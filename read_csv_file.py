# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:58:56 2021

@author: Guillem
"""

import json
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import pandas as pd

#SETTINGS JSON FILE
setting_file = "settings.json"
json_file = json.load(open(setting_file)) # Reads json file
input_folder = json_file["input_folder"]
csv_file = json_file["csv_file"]
gb_file = json_file["gb_file"]
peak_fasta_file = json_file["peak_fasta_file"]
file_witd_peakId = json_file["file_with_peakId"]

#READ SEQUENCE FROM GENBANK
record = []
print('Reading ' + gb_file)
record = SeqIO.read(input_folder + '/' + gb_file, "genbank")

#READ CSV FILE
data = pd.read_csv(csv_file)
df = pd.DataFrame(data) 
df['id'] = df.index 

#WRITE SEQUENCES INTERVALS FROM CSV AND WRITE INTO FASTA FILE
openfile = open(peak_fasta_file,'w')
for i in df.index.values:
    SeqIO.write(record[data.loc[i].start:data.loc[i].end], openfile, 'fasta')
openfile.close()
    
"""
def get_peakdata_csv_file(input_folder, gb_file, csv_file, peak_fasta_file):
    #READ SEQUENCE FROM GENBANK
    record = []
    print('Reading ' + gb_file)
    record = SeqIO.read(input_folder + '/' + gb_file, "genbank")

    #READ CSV FILE
    data = pd.read_csv(csv_file)
    df = pd.DataFrame(data) 
    df['id'] = df.index
    
    #WRITE INTO FASTA FILE
    openfile = open(peak_fasta_file,'w')
    for i in df.index.values:
        SeqIO.write(record[data.loc[i].start:data.loc[i].end], openfile, 'fasta')
    openfile.close()
    return openfile
"""