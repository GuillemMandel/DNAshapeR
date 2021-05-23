# -*- coding: utf-8 -*-
"""
Created on Tue May 11 02:08:52 2021

@author: Guillem
"""

from Bio import SeqIO

import csv
import json
import sys
import os

def read_gb_file(input_folder, gb_file):
    record = []
    print('Reading ' + gb_file)

    record = SeqIO.read(input_folder + '/' + gb_file, "genbank")

    return record

def read_csv_file(input_folder, csv_file, col_start, col_end):
    record_seq = []
    
    # Read the file content
    with open(csv_file, "r", encoding='utf-8', errors='ignore') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                record_seq.append(row[col_start:col_end])
            line_count += 1
        
        length = len(record_seq)
        # Writes the accessions in the required format
        accessions = ('[')
        for element in record_seq:
            accessions += '["' + str(element) + '"]'
            if line_count < length:
                accessions += ', '
            line_count += 1
        accessions += (']')

    return accessions

                  

if __name__ == '__main__':

    # Configuration file
    setting_file = "conf_file_inputs.json"
    try:
        json_file = json.load(open(setting_file)) # Reads json file
    except IOError:
        sys.exit('Could not open conf_file_inputs.json')

    # Important folders
    input_folder = json_file["input_folder"]
    if not os.path.exists(input_folder):
        os.mkdir(input_folder)
    output_folder = json_file["output_folder"]
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)        
        
    user_email = json_file["user_email"]
    accessing_list = json_file["genome_accessions"]
    csvFile = json_file["csv_file"]
    start = json_file["col_start"]
    end = json_file["col_end"]
    fastaFile = json_file["fasta_file"]
    gb_file = json_file["gb_file"]

    print(read_gb_file(input_folder, gb_file))
    