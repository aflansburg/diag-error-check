# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:53:21 2015

@author: abram
"""
import re
import csv
import sys

fp = sys.argv[0]

regex = re.compile(ur'^(.*?)(error count = )(1?[1-9])', re.IGNORECASE)

log_text_rows = []

with open(fp) as input_file:
    for row in csv.reader(input_file):
        log_text_rows.append(row)

store_error_i = []
for i in log_text_rows:
    thisStr = str(i)
    check_errors = re.search(regex, thisStr)
    if check_errors:
        store_error_i.append(check_errors.group(3))

error_count = 0
for e in store_error_i:
    error_count += int(e)

print 'Total Error Count: ', error_count
                             