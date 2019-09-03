import pandas
import sys

KEY_START = '<string name="{}">'
KEY_END = '</string>'
result = ""
print(sys.getdefaultencoding())
csv = pandas.read_csv("strings.csv")
for index, row in csv.iterrows():
    start = KEY_START.format(row[0])
    result = result + start + row[1] + KEY_END + '\n'
result.encode("GBK", 'ignore')
print(result)
with open('strings.xml', 'w', encoding='utf-8') as f:
    f.write(result)
f.close()