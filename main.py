seq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCATGATAGGGTCATAGACCCTAGATGCAGATGACACGATTGCTGCTCGTGCTGCTGGGCATAGACATAGACATAGACCCTTGACATAGCAGATAGACAGATGCAGATAGACATTGACAGATAGACATGGCAGATACAGGTAGACATAGACATTGACATAGACATAGACATAGACGTGATAGACCGACGAGCAGAAGATAGACATATAGATAGATAGAGATATATAGACA'
seq = seq.replace('A','t')
seq = seq.replace('T','a')
seq = seq.replace('C','g')
seq = seq.replace('G','c')
print(seq.upper())

