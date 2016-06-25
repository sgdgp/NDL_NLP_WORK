import json

def ngrams(input, n):
	input = input.split(' ')
  	output = []
  	for i in range(len(input)-n+1):
		output.append(input[i:i+n])
  	return output
	  
	  
def main():
	fin_name = "cayasongi.txt"
	fin = open(fin_name,'r')
	out = {}
	for row in fin:
		row = row.strip()
		out = ngrams(row,1)	
	fout = open('n_gram_unigram.json'.'w')
	json.dump(out,fout)	