package test;

import java.util.concurrent.*;
import applications.Decomposer;
import donnees.DonneesLinguistiquesAbstract;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.*;
import java.util.*;

public class Test_Decomposer {

	public static String[] problems = {"qujalisgujjivugut",
			"sivulliujjijariaqarnirmut",
			"aullaujjijinut",
			"nuqqaujjijunit",
			"nuqqaujjigunnangittuq",
			"angunasuaqrujjiniarlutik",
			"tuksiujjivattunik"};
	/**
	 * @param args
	 */
	public static void main(String[] args) {

		DonneesLinguistiquesAbstract.init(); // initialize the linguistic database
		Scanner scan = new Scanner(System.in);
		BufferedWriter bw = null;

		try (BufferedReader br = new BufferedReader(new FileReader("10k_files/04.txt"))) {
			FileWriter min_printer = new FileWriter(new File("10k_output/min_output_04.txt"), true);
			FileWriter max_printer = new FileWriter(new File("10k_output/max_output_04.txt"), true);
			String line;
			int counter = 0;
			int start = 886;
			while ((line = br.readLine()) != null) {
				counter++;
				System.out.println(counter);
				if (counter >= start) {

          // IF LINE IS NEWLINE, JUST WRITE TO FILE

					if (line.equals("\n")) {		
						min_printer.write("\n");
						min_printer.flush();
						max_printer.write("\n");
						max_printer.flush();
					} else {
						
            // SPLIT SENTENCE INTO STRING ARRAY
						
            			String[] min_split = sentenceToArray(line);
						String[] max_split = sentenceToArray(line);
						
            // FOR EACH STRING IN ARRAY, REPLACE WITH DECOMP IF POSSIBLE
						
			            for (int i = 0; i < min_split.length; i++) {
							String word = min_split[i];

							Pattern p = Pattern.compile("[%]");
							String decomp = "";
							boolean hasSpecialChar = p.matcher(word).find();
							if (Arrays.asList(problems).contains(word)) {
			                  //
			                } else if (hasSpecialChar || word.contains("jji")) {
			                  //
			                } else {
			                  // Timeout code
			                  try {
			                    decomp = timeLimitedDecompose(word);
			                  } catch (Exception e) {
			                    System.out.println("Exception thrown");
			                  }
			                  String min_selected = selectDecomp(decomp, 0);
			                  String max_selected = selectDecomp(decomp, 1);
			                  if (!min_selected.equals("")) {
			                    min_split[i] = min_selected;
			                    max_split[i] = max_selected;
			                  }
			                }
			            }
            			// JOIN DECOMPOSED STRINGS AND WRITE LINE TO FILE
					String min_joined = String.join(" ",min_split);
					String max_joined = String.join(" ",max_split);
					// Replace double spaces with single
					min_joined = min_joined.replaceAll("  "," ");
					max_joined = max_joined.replaceAll("  "," ");
					min_printer.write(min_joined + "\n");
					min_printer.flush();
					max_printer.write(max_joined + "\n");
					max_printer.flush();
					}
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

  private static String timeLimitedDecompose(String word) throws Exception {
    final long startTime = System.currentTimeMillis();
    // log(startTime, "calling runWithTimeout!");
    try {
      TimeLimitedCodeBlock.runWithTimeout(new Runnable() {
        @Override
        public void run() {
          try {
            String test = Decomposer.decomposeToMultilineString(word);
          }
          catch (Exception e) {
            log(startTime, "was interrupted!");
          }
        }
      }, 1, TimeUnit.SECONDS);
    }
    catch (TimeoutException e) {
      // If timeout, just return word
      return word;
    }
    // If no timeout, return decomposition
    return Decomposer.decomposeToMultilineString(word);
  }

  private static void log(long startTime, String msg) {
    long elapsedSeconds = (System.currentTimeMillis() - startTime);
    System.out.format("%1$5sms [%2$16s] %3$s\n", elapsedSeconds, Thread.currentThread().getName(), msg);
  }

	/* Function: selectDecomp()
	 * This function takes in the morphological analyzer output,
	 * splits it into candidate parsings, compute the length of each 
	 * candidate parsing (in number of morphemes) and returns the lowest
	 * or highest parsing, min index.
	 *
	 * # option 0 = min
	 * # option 1 = max
	 */ 
	private static String selectDecomp(String choice_str, int option) {
		String[] choice_arr = choice_str.split("\\n+");
		String[] parsed_arr = new String[choice_arr.length];
		int[] length_arr = new int[choice_arr.length];
		/* Parse each string and compute length of parsing */
		for (int i = 0; i < choice_arr.length; i++) {
			String parsed = parseString(choice_arr[i]);
			parsed_arr[i] = parsed;
			length_arr[i] = parsed.split("\\s+").length;
		};
		if (option == 0) {
			// Find minimum
			int minIndex = findSmallest(length_arr);
			return parsed_arr[minIndex];
		} else {
			int maxIndex = findMax(length_arr);
			return parsed_arr[maxIndex];
		}
	}

	/* Finds index of min elem in int array */
	private static int findSmallest(int[] arr) {
		int index = 0;
		int min = arr[index];
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] < min) {
				min = arr[i];
				index = i;
			};
		};
		return index;
	};

	/* Finds index of maximum elem in int array */
	private static int findMax(int[] arr) {
		int index = 0;
		int max = arr[index];
		for (int i = 1; i < arr.length; i++) {
			if (arr[i] > max) {
				max = arr[i];
				index = i;
			};
		};
		return index;
	};

	/* For debugging */
	private static void printArray(String[] arr) {
		String joined = String.join(" ",arr);
		System.out.println(joined);
	}

	/* Function: sentenceToArray()
	 * This function takes in a sentence and breaks it into an array of strings.
	 * Uses space '\s' as delimiter.
	 */
	private static String[] sentenceToArray(String sentence) {
		String[] words = sentence.split("\\s+");
		return words;
	}

	/* Function: parseString()
	 * This function is intended to take in a parsed string from the morphological
	 * analyzer and return a space delimited version of the original words parsed
	 * into component morphemes.
	 */ 
	private static String parseString(String value) {
		String word = value;
		// trims everything after between colon and }"
		word = word.replaceAll(":[/&0-9a-z\\-]+\\}", " ");
		word = word.replaceAll("\\{","");
		return word;
	}
}
