#!/bin/bash
# Program: This program shows "Output CPU Info" on the screen
# History: 2017/04/21 Victor First release

echo "processing..."
top -F -R -o cpu > data.txt

exit 0