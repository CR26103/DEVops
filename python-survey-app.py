from reader import read_csv, write_csv, append_csv

print(read_csv())
write_csv([1,2,3,4,5])
print(read_csv())
append_csv([6,7,8,9,10])
print(read_csv())
