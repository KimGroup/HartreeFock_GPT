#!/bin/bash

original_string="Convert noninteracting Hamiltonian in real space to momentum space"
replacement_string="Convert noninteracting Hamiltonian in real space to momentum space"

grep -rn --include=\*.md './' -e "$original_string"

# grep -rnl --include=\*.md './' -e "$original_string" | while read -r file ; do 
#     sed -i "s/$original_string/$replacement_string/g" "$file"
# done