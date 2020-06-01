#!/usr/local/bin/python3
import json
from json2xml import json2xml

# a Python object (dict):
x = {
  "name": "Manoj",
  "age": 29,
  "city": "Hyderabad"
}

#format JSON to a different representation
y=json.dumps(x, indent=4, separators=(";", " = "))

# the result is a JSON string:
print(y)

# Conver x to xml
z = json2xml.Json2xml(x).to_xml()
