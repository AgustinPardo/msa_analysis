#! python3
from Bio import SeqIO
import sys
entrada_file=sys.argv[1]
salida_name=entrada_file.split(".")[0]
salida_file=open(salida_name+".rep_5_percent.out","w")

def countLetters(list,divisor):
	uniques=set(list)
	out_list=[]
	for element in uniques:
		count = column_letters.count(element)
		proportion=count*100/divisor
		if proportion>5 and element != "X":
			out_list.append(element + ": "+ "{0:.3f}".format(proportion)) 
	return out_list
	
sequences={}
for record in SeqIO.parse(entrada_file, 'fasta'):
	sequences[record.description]=record.seq
	largo_seqs=len(record.seq)

column_letters=[]

column_dif=0
for i in range(largo_seqs):
	column_letters=[]
	for seq in sequences:
		secuencia=sequences[seq]
		column_letters.append(secuencia[i])

	if (("X" in column_letters and len(set(column_letters))>2) 
		or ("X" not in column_letters and len(set(column_letters))>1)):

		# print(column_letters)
		countLetters_list=countLetters(column_letters,3328)

		if len(countLetters_list)>1:
			salida_file.write(">Posicion: " + str(i+1)+"\n")
			countLetters_list='\n'.join(countLetters_list)
			salida_file.write(countLetters_list+"\n")
			column_dif=column_dif+1
		
salida_file.write("Cantidad de columnas con variantes: "+ str(column_dif)+"\n")
salida_file.write("cantidad de secuencias: 3328"+"\n")
salida_file.write("Largo de las secuencias: 76")