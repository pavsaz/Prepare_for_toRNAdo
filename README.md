This script is required to generate input files for toRNAdo script.

Usage: python Prepare_for_toRNAdo.py directory fasta_file gff_file

The requirements for the script are:

1. A directory containing your sorted bam files. IMPORTANT: The file names must end in ".sorted.bam".
2. A fasta file of your genome, to which you mapped RNA-Seq reads.
3. A gff file of your genome. Make sure that GFF file doesn’t contain nucleotide sequence at the end of the file. Also make sure that there is no feature in a GFF file that covers the whole genome - that would normally be the very first feature. 

IMPORTANT: Use Prepare_for_toRNAdo_v1 for Bedtools version below 2.24.0 and Prepare_for_toRNAdo_v2 for Bedtools version 2.24.0 and above.

This script outputs directories for each of the sorted bam files, containing input files for toRNAdo. These directories are produced in the same directory as the script.
