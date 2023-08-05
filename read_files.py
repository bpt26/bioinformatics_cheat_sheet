import sys
import os
import io
import pandas
import numpy as np
import gtfparse
from scipy import stats
from Bio import Seq
from Bio import SeqIO

def read_bed6(filename):
    # Read in .bed file following .bed format:
    # https://genome.ucsc.edu/FAQ/FAQformat.html#format1
    # These files have no headers, so we specify the names of the columns, and ensure that coordinates ints
    return pandas.read_csv(filename,sep='\t',names=['chr','start','end','name','score','strand'])

def read_bed12(filename):
    # Similar to read_bed6(), follows .bed format with all optional fields
    # https://genome.ucsc.edu/FAQ/FAQformat.html#format1
    return pandas.read_csv(filename,sep='\t',names=['chr','start','end','name','score','strand',
    	'thickStart','thickEnd','rgb','blockCount','blockSizes','blockStarts'])

def read_blast_output(filename):
    # If a BLAST search is run with the flag -outfmt 6, the results are tab-separated,
    # and have the column headers specified in this function
    # For more information, see: https://www.metagenomics.wiki/tools/blast/blastn-output-format-6
    return pandas.read_csv(filename,sep='\t',names=['qseqid','sseqid','pident','length','mismatch','gapopen',
        'qstart','qend','sstart','send','evalue','bitscore'])

def read_fasta(filename):
	# This function uses the SeqIO library to parse a .fasta file
	# .fasta files have a sequence_id and a sequence, and this file
	# outputs the .fasta in DataFrame format
	# https://en.wikipedia.org/wiki/FASTA_format
    temp_dict = SeqIO.to_dict(SeqIO.parse(fasta_file, 'fasta'))
    df = pandas.DataFrame(temp_dict.keys(),columns=['id'])
    df['sequence'] = df['id'].apply(lambda x: str(temp_dict[x].seq.upper()))
    return df

def read_gtf(filename, detailed=True):
	# This function wraps the gtfparse functions for
	# reading in a .gtf file. This file type is used for 
	# annotating genes, transcripts, exons, and other genomic features.
	# https://useast.ensembl.org/info/website/upload/gff.html
	if detailed:
		return gtfparse.read_gtf(filename)
	else:
		return gtfparse.parse_gtf(filename)