import csv
import os
import sys
from pprint import pprint as pp


try:
	
	myListOfDict = []
	header = []
	with open("Ques_2.csv", mode="r") as input_file_pointer:
		my_reader = csv.reader(input_file_pointer)
		header = my_reader.__next__()
		for row in my_reader:
			myListOfDict.append(dict(zip(header,row)))
		
		pp(myListOfDict[1:5])
	
	with open("practice_2.csv", mode="w", newline="") as output_file_pointer:
		my_writer = csv.DictWriter(output_file_pointer, fieldnames = header)
		my_writer.writeheader()
		for row in myListOfDict:
			my_writer.writerow(row)
			
except Exception as e:
	exc_type, exc_obj, exc_tb = sys.exc_info()
	fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	print('{}: Error on line {}'.format(fname, exc_tb.tb_lineno), type(e).__name__, e)
