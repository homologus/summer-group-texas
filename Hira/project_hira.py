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



def findName(gff):
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
            if resWor[2] == "CDS":
                plusMinus.append(resPun[resPun.index( resWor[4]) + 1].strip() )
    return plusMinus


def reverseComplement(str):
    newString = ""
    for char in str:
        if char == 'A':
            newString = 'T' + newString
        elif char == 'T':
            newString = 'A' + newString
        elif char == 'G':
            newString = 'C' + newString
        elif char == 'C':
            newString = 'G' + newString
    return newString



def transverse(str):
    newString = ""
    for char in str:
        if char == 'A':
            newString = newString + 'T'
        elif char == 'T':
            newString = newString + 'A'
        elif char == 'G':
            newString = newString + 'C'
        elif char == 'C':
            newString = newString + 'G'
    return newString




def convertProtein(str):
    protein = ""
    codes = {
            'aaa': 'K', 'aac': 'N', 'aag': 'K', 'aau': 'N', 'aca': 'T', 'acc': 'T', 'acg': 'T', 'acu': 'T', 'aga': 'R', 'agc': 'S', 'agg': 'R',
            'agu': 'S', 'aua': 'I','auc': 'I', 'aug': 'M', 'auu': 'I', 'caa': '0', 'cac': 'H', 'cag': '0', 'cau': 'H', 'cca': 'P', 'ccc': 'P', 
            'ccg': 'P', 'ccu': 'P', 'cga': 'R', 'cgc': 'R', 'cgg': 'R', 'cgu': 'R', 'cua': 'L', 'cuc': 'L', 'cug': 'L', 'cuu': 'L', 'gaa': 'E', 
            'gac': 'D', 'gag': 'E', 'gau': 'D', 'gca': 'A', 'gcc': 'A', 'gcg': 'A', 'gcu': 'A', 'gga': 'G', 'ggc': 'G', 'ggg': 'G', 'ggu': 'G', 
            'gua': 'V', 'guc': 'V', 'gug': 'V', 'guu': 'V', 'uaa': '_', 'uac': 'Y', 'uag': '_', 'uau': 'Y', 'uca': 'S', 'ucc': 'S', 'ucg': 'S',
            'ucu': 'S', 'uga': '_', 'ugc': 'C', 'ugg': 'W', 'ugu': 'C', 'uua': 'I', 'uuc': 'F', 'uug': 'L', 'uuu': 'F'
    }

    for i in range(0, len(str), 3):
        codon = str[i : i + 3].lower().replace('t', 'u')
        protein = protein + codes[codon]
    return protein


with open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.fna", "r") as f:
    fasta = f.read()

with open("/share/Ecoli/GCA_000005845.2_ASM584v2_genomic.gff", "r") as f:
    gff = f.readlines()

fasta = fasta[fasta.index("\n"):]
fasta = fasta.replace("\n", "")

startEnd = findStartEnd(gff)



#for i in range(200, 300, 1):
#	print(startEnd[i])

proteinDNA = []


for index, key in enumerate(startEnd):
    if (key[1] - key[0] + 1)%3 == 0:
        proteinDNA.append(fasta[key[0] - 1: key[1]])
    


reverse = shouldReverse(gff)
for i, string in enumerate(proteinDNA):
    if reverse[i][2] == '-':
        proteinDNA[i] = reverseComplement(proteinDNA[i])

proteins = []
for i,key in enumerate(proteinDNA):
        if (startEnd[i][1] - startEnd[i][0] + 1)%3 == 0:
            proteins.append(convertProtein(key))
#            print(proteins[i] , "\n", proteinDNA[i] , "  ", startEnd[i] ,"\n\n\n\n")

print( proteins)






#>lcl|U00096.3_cds_236 [gene=crl] [locus_tag=b0240] [db_xref=ASAP:ABE-0000821,ECOCYC:EG11092,EcoGene:EG11092] [protein=RNA polymerase holoenzyme assembly factor Crl] [ps
#eudo=true] [location=join(257829..257899,258676..259006)] [gbkey=CDS]
#ATGACGTTACCGAGTGGACACCCGAAGAGCAGATTGATCAAAAAATTTACCGCACTAGGCCCGTATATTCGTGAAGGTAA
#GTGCAAAGATAATCGATTCTTTTTCGATTGTCTGGCTGTATGCGTCAACGTGAAACCGGCACCGGAAGTGCGTGAATTCT
#GGGGCTGGTGGATGGAGCTGGAAGCGCAGGAATCCCGTTTTACCTACAGTTACCAGTTTGGTCTGTTCGATAAAGCAGGC
#GACTGGAAGAGTGTTCCGGTAAAAGACACTGAAGTGGTTGAACGACTGGAGCACACCCTGCGTGAGTTTCACGAGAAGCT
#GCGTGAACTGCTGACGACGCTGAATCTGAAGCTGGAACCGGCGGATGATTTTCGTGACGAGCCGGTGAAGTTAACGGCGT
#GA




