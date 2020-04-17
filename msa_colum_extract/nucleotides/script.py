import pandas as pd
from Bio import SeqIO

def createMatrix(inFile):
    MSA=SeqIO.parse(inFile, 'fasta')
    MSA_raw=[list(rec.seq) for rec in MSA]
    MSA_df=pd.DataFrame(MSA_raw)
    return MSA_df

#la funcion para pedir valores por columna es dataframe.value_counts()
#que recuerde es basicamente un diccionario de python
#podes pedir los indices de ese diccionario con dataframe.value_counts().index

"""La idea es que para cada columna del MSA revises si esta conservada o no.
Si esta conservada, en el index del value_counts() deberias ver solo una letra
de nucleotido (A, T, C o G), si no lo esta, deberias ver al menos dos (por ejemplo
que haya T y C, o G y T, etc...). Ignora el hecho de que haya missing data (N)
o gaps(-), que encuentres dos letras tipo nucleotido en el index de una columna
es codicion suficiente para decir que hay snps"""

#pseudocodigo
"""for columna in MSA:
        if columna.value_counts().index has 2 letters of [A,T, C, G]
            keep columna"""
