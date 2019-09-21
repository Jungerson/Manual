#!/usr/bin/env python

import sys
import csv
import json
import boto3

if len(sys.argv) != 3:
  print("Usage: python3 insert_items.py <csv file> <deploy stage>")
  sys.exit(-1)

client = boto3.client('dynamodb', region_name='us-east-1')

csv_file = sys.argv[1]
stage = sys.argv[2]

with open(csv_file) as f:
  reader = csv.reader(f, delimiter=",")
  line = 0
  data = {}

  for row in reader:
    line = line + 1

    if line == 1:
      data_type = row
    elif line == 2:
      header = row
    else:
      c = 0
      for col in row:
        if data_type[c] == 'BOOL':
          if col == "1":
            col = True
          else:
            col = False

        data[header[c]] = { data_type[c]: col }
        c = c + 1
      print(data)
      response = client.put_item(
          TableName = 'VisionAware-' + stage,
          Item = data
        )
      

  