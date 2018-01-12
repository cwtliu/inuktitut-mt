grep -n '^$' english_ver2_oct16.txt
lines=$(grep -n '^$' english_ver2_oct16-1.txt)

echo $lines >> lines.txt

sed 's/\\n/\'$'\n''/g' lines.txt


output=$(awk ‘NR==FNR{n[$1];next}!(FNR in n)’ empty_lines.txt english_multipleperiodsremoved.txt>test.txt)

echo $output >> output.txt




