MY_PATH="`dirname \"$0\"`"
FILE="access.log"
OUTPUT_FILE="bash.log"
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"
MY_PATH="${MY_PATH}/${FILE}"
if [ -z "$MY_PATH" ] ; then
  echo 'No access.log file'
  return
fi

echo 'Number of requests' > $OUTPUT_FILE
cat $MY_PATH  | wc -l >> $OUTPUT_FILE

echo 'Number of requests type' >> $OUTPUT_FILE
awk '{ print $6 }' $MY_PATH | sort | uniq -c | sed -r 's/\"//' | awk '{ if ($2 ~ /^[A-Z]+$/) print}' >> $OUTPUT_FILE

echo 'Top 10 requests with the longest content length' >> $OUTPUT_FILE
awk -F\" 'NR == FNR { T[$4]++; next } {print $4, T[$4], $3}' $MY_PATH $MY_PATH | sort -k4 -n -r | awk '{ if ($1 != "-") print $1, $3, $2}' | head -10 >> $OUTPUT_FILE


echo 'Top 10 requests with client error' >> $OUTPUT_FILE
 awk -F\" 'NR == FNR { T[$4]++; next } {print $4, T[$4], $3, $1}' $MY_PATH $MY_PATH | awk '$3 ~ /^4[0-9][0-9]$/' | sort -k2 -n -r | awk '{ if ($1 != "-") print $1, $3, $5}' | head -10 >> $OUTPUT_FILE

echo 'Top 10 requests with server error' >> $OUTPUT_FILE
   awk -F\" 'NR == FNR { T[$4]++; next } {print $4, T[$4], $3, $1}' $MY_PATH $MY_PATH | awk '$3 ~ /^5[0-9][0-9]$/' | sort -k2 -n -r | awk '{ if ($1 != "-") print $1, $3, $5}' | head -10 >> $OUTPUT_FILE
