from Bio import SeqIO
import re
import os
genome_list = os.listdir('/export/data1/db/img/07042014/genomes/')
genome_list.remove('lala')
out_file = '/home/gray/CxxCH/totals.csv'
out_file2 = '/home/gray/CxxCH/all.csv'
output_handle = open(out_file,'w')
output_handle2 = open(out_file2,'w')
for genome in genome_list:
        path = '/export/data1/db/img/07042014/genomes/'+genome
        contents = os.listdir(path)
        if genome + '.genes.faa' in contents:
                input_file = path + '/' + genome + '.genes.faa'
                records = SeqIO.parse(open(input_file,'rU'), 'fasta')
                p = re.compile('c..ch',re.IGNORECASE)
                counter = 0
                counter2 = 0
                counter3 = 0
                largest = 0
                output_handle2.write(genome+',')
                os.mkdir('/home/gray/CxxCH/genomes/101914/' + genome)
                out_file3 = '/home/gray/CxxCH/genomes/101914/' + genome + '/' + genome + '_cxxch.faa'
                output_handle3 = open(out_file3,'w')
                for record in records:
                        counter2+=1
                        sequence = str(record.seq)
                        if len(p.findall(sequence))>0:
                                if len(p.findall(sequence))>largest:
                                        largest = len(p.findall(sequence))
                                counter+=1
                                if len(p.findall(sequence))>8:
                                        counter3+=1
                                output_handle3.write('>'+record.name+'$$'+str(len(p.findall(sequence)))+'\n')
                                output_handle3.write(sequence)
                                output_handle3.write('\n')
                                output_handle2.write(record.name+','+str(len(p.findall(sequence)))+',')
                output_handle3.close()
                output_handle2.write('\n')
                print genome, counter, 'of', counter2, 'most CXXCHs:',largest
                output_handle.write(genome+','+str(largest)+','+str(counter3)+','+str(counter)+','+str(counter2)+'\n')
output_handle.close()
output_handle2.close()