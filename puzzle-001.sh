#!/bin/bash

elfs=()
tmp=0

input="./puzzle-001-input.txt"
while IFS= read -r line
do
  if [ "$line" = "" ]; then
    elfs+=($tmp)
    tmp=0
  else
    tmp=$((tmp+line))
  fi
done < "$input"

IFS=$'\n' sorted=($(sort -nr <<<"${elfs[*]}"))
unset IFS

let top3=(${sorted[0]} + ${sorted[1]} + ${sorted[2]})

echo "Best #1 ${sorted[0]}"
echo "Best #3 ${top3}"

#echo "${sorted[@]}\n"
