import re
import string

def findStartEnd(gff):
    startEnd = []
    for i, x in enumerate(gff):
        if x[0] != '#' :
            res = re.sub('['+string.punctuation+']', '', x).split()
            if res[2] == "CDS":
                startEnd.append(( int(res[3]), int(res[4]) ))
    return startEnd




def shouldReverse(gff):
    plusMinus = []
    for i, x in enumerate(gff):
        if x[0] != '#' :
            resPun = re.split(r'(\W+)', x)
            resWor = re.sub('['+string.punctuation+']', '', x).split()

            if resWor[1] == "CDS":
                print("word")
                plusMinus.append( resPun.index( int(resWor[4]) ) )
    return plusMinus



with  open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna", "r") as f:
    fasta = f.read()

with open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.gff", "r") as f:
    gff = f.readlines()

fasta = fasta.replace("\n", "")

startEnd = findStartEnd(gff)

proteinDNA = [];

for index, key in enumerate(startEnd):
    proteinDNA.append(fasta[key[0] - 1: key[1]])

print(shouldReverse(gff))
