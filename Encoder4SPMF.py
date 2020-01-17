#!/usr/bin/env python
# coding: utf-8
# Usage : python <File-to-encode> <encoded-file>
# Usage : python <File-to-encode> (write in GrandEst_encoded_for_SPMF.txt)


import pandas
import csv
import sys
import pickle


p=len(sys.argv)
print(p)

if p==3:
    f_out=sys.argv[2]
else:
    f_out="GrandEst_encoded_for_SPMF.txt"
    
# read the GrandEst csv file
f_in=sys.argv[1]
csv_df = pandas.read_csv(f_in,sep=';',low_memory=False)
    
# drop the unwanted columns
list_2_drop = ['NUMMR','ACHLR','AEMM','AEMMR','AGED','AGEREV','AGEREVQ','ANAI','ANEM','APAF','ARRIVR','CATPC','CHAU','CHFL','CS2','CS3','CUIS','DEPT',
               'DEROU','EAU','EGOUL','ELEC','EPCI','HLML','ILETUD','ILETUU','ILT','INAI','INPER','INPERF','IPONDI','IRAN','IRANUU','LIENF','LPRF','LPRM',
               'METRODOM','NA88','NAF08','NAIDT','NAT13','NAT49','NATN12','NATN49','NUMF','ORIDT','PNAI12','PROF','RECH','SANIDOM','STAT','STAT_CONJ',
               'SURF','TACTD16','TP','TRANS','TYPC','TYPFC','TYPL','TYPMD','TYPMR','UR','WC']
new_csv_df = csv_df.drop(list_2_drop, axis=1)
# save this new dataframe to another CSV, not to mess the original GrandEst csv
new_csv_df.to_csv(r'cleaned_GrandEst.csv',index = None, header=False)

 # transform the csv to txt
with open("cleaned_GrandEst.txt","w+") as output_file:
    with open("cleaned_GrandEst.csv","r") as input_file:
        [output_file.write(" ".join(row)+'\n') for row in csv.reader(input_file)]
        output_file.close()
        
# Construction du dictionnaire
dico={}
invdico={}
indice=1
f=open("cleaned_GrandEst.txt",'r')
for line in f.readlines():
    line=line.rstrip()
    print(line)
    for i,e in enumerate(line.split(' ')):
        a=str(i)+"-"+e
        if a not in dico.keys():
            print(a)
            dico[a]=indice
            invdico[indice]=a
            indice +=1
f.close()

print(dico)


# construction du fichier de donnees
out=open(f_out,'w')
f=open("cleaned_GrandEst.txt",'r')
for line in f.readlines():
    line=line.rstrip()
    l=[]
 #   print line
    for i,e in enumerate(line.split(' ')):
        a=str(i)+"-"+e
        l.append(dico[a])
    l.sort()
    l2=[str(i) for i in l]


#    input("xxx :")
#    out.write
    #out.write("{"+",".join(l2)+"}")
    out.write(" ".join(l2))
    out.write("\n")
f.close()

fichier=open('invdico.dbm', 'wb')
pickle.dump(invdico,fichier)




