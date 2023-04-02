from reader import read_csv, write_csv, append_csv
import csv
import pandas

assert  len(read_csv()) != 0


assert len(read_csv()) < len(write_csv([1,2,3,4,5]))


