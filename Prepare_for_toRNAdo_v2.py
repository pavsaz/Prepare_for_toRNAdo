#IMPORTANT: Only use with BEDtools version 2.24.0 and above

import os
from sys import argv

script, folder, fasta_file, gff_file = argv

for filename in os.listdir(folder):
    if filename.endswith(".sorted.bam"):
        namefile = filename.replace(".sorted.bam", "_ncoverage.txt")
        folder_name = filename.replace(".sorted.bam", "")
        os.system("mkdir " + folder_name)
        os.system("coverageBed -s -d -b " + folder + filename + " -a " + gff_file + " -sorted > " + folder_name + "/" + namefile)
        namefile1 = filename.replace(".sorted.bam", "_nboth.txt")
        os.system("genomeCoverageBed -ibam " + folder + filename + " -g " + fasta_file + " -d > " + folder_name + "/" + namefile1)
        namefile2 = filename.replace(".sorted.bam", "_nminus.txt")
        os.system("genomeCoverageBed -ibam " + folder + filename + " -g " + fasta_file + " -d -strand - > " + folder_name + "/" + namefile2)
        namefile3 = filename.replace(".sorted.bam", "_nplus.txt")
        os.system("genomeCoverageBed -ibam " + folder + filename + " -g " + fasta_file + " -d -strand + > " + folder_name + "/" + namefile3)
        for filename1 in os.listdir(folder_name):
            if filename1.endswith("ge.txt"):
                namefile = filename1.replace(".txt", "1.txt")
                os.system("cut -f 4,7,10,11 ./" + folder_name + "/" + filename1 + " > ./" + folder_name + "/" + namefile)
        for filename2 in os.listdir(folder_name):
            if filename2.endswith("oth.txt"):
                namefile1 = filename2.replace(".txt", "1.txt")
                os.system("cut -f 2,3 ./" + folder_name + "/" + filename2 + " > ./" + folder_name + "/" + namefile1)
        for filename3 in os.listdir(folder_name):
            if filename3.endswith("us.txt"):
                namefile2 = filename3.replace(".txt", "1.txt")
                os.system("cut -f 2,3 ./" + folder_name + "/" + filename3 + " > ./" + folder_name + "/" + namefile2)

