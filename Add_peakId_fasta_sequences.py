# -*- coding: utf-8 -*-
"""
Created on Sun May 23 18:13:16 2021

@author: Guillem
"""

import sys 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

original_file = r"peak_fasta_file"
corrected_file = r"peak_fasta_file_id"
           
with open(original_file) as original, open(corrected_file, 'w') as corrected:
    records = SeqIO.parse(original_file, 'fasta')
    records_seq=[]
    i = 0
    for record in records:
        seq_id = 'peak_%i' %i
        record_d = SeqRecord(record.seq, seq_id, '', record.description)
        i = i +1
        records_seq.append(record_d)
    SeqIO.write(records_seq, corrected, "fasta")
    
corrected.close()