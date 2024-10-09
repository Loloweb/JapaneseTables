import csv

with open('./tables/hiragana.csv', mode='r') as infile:
    reader = csv.reader(infile)
    hiragana = {rows[0]:rows[3] for rows in reader}

romanji=[]
with open('./tables/romanji.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for i, row in enumerate(reader):
        if 2 <= i <= 5:
            romanji.append(row)

print(hiragana)
print(romanji)