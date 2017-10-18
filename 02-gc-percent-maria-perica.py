
# coding: utf-8

# In[13]:

#First 100 nucleotides of H1N1 virus
flu_ns1_seq = "GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA"

#Count the "C" nucelotides in the sequence
c_nuc = flu_ns1_seq.count('C')


#Count the "G" nucleotides in the sequence
g_nuc = flu_ns1_seq.count('G')


#Add C and G nucleotides together
CG = c_nuc + g_nuc


#Count the number of total nucleotides
total = len(flu_ns1_seq)


#Find percent of G and C
percent = ((CG / total) * 100)
print(percent, "% of the 100 nucleotides of the H1N1 virus sequence provided are either C or G nucleotides")


# In[ ]:
