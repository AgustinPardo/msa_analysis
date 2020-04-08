#! python3
from Bio import SeqIO

sequences={}
for record in SeqIO.parse("msa_prueba.fasta", 'fasta'):
	sequences[record.id]=record.seq
	largo_seqs=len(record.seq)

column_letters=[]

column_dif=0
for i in range(largo_seqs):
	column_letters=[]
	for seq in sequences:
		secuencia=sequences[seq]
		column_letters.append(secuencia[i]) 
	if (('a' in set(column_letters) and 'g' in set(column_letters))
	or ('a' in set(column_letters) and 't' in set(column_letters))
	or ('a' in set(column_letters) and 'c' in set(column_letters))
	or ('g' in set(column_letters) and 't' in set(column_letters))
	or ('g' in set(column_letters) and 'c' in set(column_letters))
	or ('t' in set(column_letters) and 'c' in set(column_letters))):
		print(i+1)
		#print(column_letters)
		count_A = column_letters.count("a")
		count_G = column_letters.count("g")
		count_T = column_letters.count("t")
		count_C = column_letters.count("c")
		print("a: "+str(count_A))
		print("g: "+str(count_G))
		print("t: "+str(count_T))
		print("c: "+str(count_C))
		column_dif=column_dif+1
		
print("Cantidad de columnas con variantes: "+ str(column_dif))