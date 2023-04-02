import csv

def read_csv():
    rows = []
    with open('./testFile.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            rows.append(row)
            return rows

def write_csv(row):
    with open('./testFile.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(row)
        
def append_csv(row):
    with open('./testFile.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(row)