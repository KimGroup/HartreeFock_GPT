#!/bin/bash

original_string="\`"
replacement_string="quadratic"

grep -rn --include=\*.jsonl './' -e "$original_string"

# grep -rnl --include=\*.jsonl './' -e "$original_string" | while read -r file ; do 
#     sed -i "s/$original_string/$replacement_string/g" "$file"
# done