package test;

import applications.Decomposer;
import donnees.DonneesLinguistiquesAbstract;

public class Test_printMeanings {

	/**
	 * @param args
	 */

	public static void main(String[] args) {
		DonneesLinguistiquesAbstract.init();
		String dec = "{saqqi:saqqik/1v}{ta:jaq/1vn}{u:u/1nv}{juq:juq/1vn}";
		String mngs[] = Decomposer.getMeaningsInArrayOfStrings(dec, "en", false, false);
		for (int i=0; i<mngs.length; i++)
			System.out.println(mngs[i]);
		System.out.println();
		mngs = Decomposer.getMeaningsInArrayOfStrings(dec, "en", true, false);
		for (int i=0; i<mngs.length; i++)
			System.out.println(mngs[i]);
		System.out.println();
		mngs = Decomposer.getMeaningsInArrayOfStrings(dec, "en", false, true);
		for (int i=0; i<mngs.length; i++)
			System.out.println(mngs[i]);
		System.out.println();
		mngs = Decomposer.getMeaningsInArrayOfStrings(dec, "en", true, true);
		for (int i=0; i<mngs.length; i++)
			System.out.print(mngs[i]);
		System.out.println();
		System.out.println(Decomposer.getMeaningsInString(dec, "en", false, false));
		System.out.println();
		System.out.println(Decomposer.getMeaningsInString(dec, "en", true, false));
		System.out.println();
		System.out.println(Decomposer.getMeaningsInString(dec, "en", false, true));
		System.out.println();
		System.out.println(Decomposer.getMeaningsInString(dec, "en", true, true));
		System.out.println();
	}
}
