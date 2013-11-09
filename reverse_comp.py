f = open('output.txt', 'w')


def rev(s):
	fin = ""
	for i in range(len(s)):
		fin = fin + s[len(s) - 1 - i]
	return fin

def comp(s):
	fin = ""
	for i in s:
		if i == 'A':
			fin = fin + 'T'
		elif i == 'T':
			fin = fin + 'A'
		elif i == 'C':
			fin = fin + 'G'
		elif i == 'G':
			fin = fin + 'C'
	return fin



f.write(rev(comp('GCACCTTCGAGAACGCGACCAATGTCAACCCACTTCTTTCCTGAGCTTGTCACATAAGGGTACACGGAACGCCCGGATAAGGAACGCCCTGCTGCTATCCATTTCACGTCACCTGTCCACGGCCGTTCGGCATAGAGATTTTCCGAGCGCCGAGCCACCTAAGGGTATCCGTCTAGCCGCAGGTTAGTTGCAGTTAGTGTTGCTAACGTCAATGCCAACATTACCATCCAAGTGTAAACCGAGCTTTTACACGTACACAGGTTTATCAAGGACGAAAGGGATCAACGGTTGAGAGATATCCAGTCTTGGCGAACGTATCTTAGTTGCGCAGACTAAAGAGGGGGACCCCTTTAACTATCTGTAGAATTTCATTAGTTTCCGCGGTGTTATATATTAATGCATGATTATCCAACTAGGACTGCTATCCTCGGCCACAACAGGAAGCTCACCTAAAAAAGGCAAGACTGCCGCCTACTGTGTTGCGGTTGTGAAGTGTGAAGTAATGAAGCCATCACAGCAAACTCACTGTGGGGTGGCCTCTGCAATCGACATGCGTCTCGGGTCGGATCATGGTATGGTCACCAGCACCCTTCATAAAGGATGTAGCCTGCGTTACAAGTAGTACTCTGGATGAGTGGAAGGAGACAGTACGATCGTTACCCGATGTATGAATTACTGCACAGATGCGCGCAAAAACTAGTAATAGGTAGCTGTTTTCACCCTATTGTGTATCTTCCCACCAGCTTGGTTGCATTCTCACCGATTTACCGCTTTGCGGCATTAACTACTAGGTGCGCTAGAAGGCAACGCCACCCACAGCACGCAGGTTGCCCGCGATTTGACTGCCTGGATCGTAGCGCTTATCGGTCCCGTCAGCCATTAATGACTGTTTCGTTAGGGATCTGCGCGCACGCGGGCAACTATCCCCCCCACTCAGCCCAATGGTTACTTAGGTCGTAATTGGGGTCAAATCCTTTCACCTGGGCACTAATGGTCATGAGCGCTGCCCGTGAGCTTCATCGAAAATCACCCAAACCCCCGCAGGGTATGCGGAAGTAGGAATCTAAAGCGTGACCGGGCGATGCGGAAATACTTAACGTTTAGTAGTCCCCCCTTAGGTAAGGGCGTCATAGTTAGAATTCGTACGTTCCTTTAAAGCCTTCTTACCATTGACTGGGTTCGATGAAACCGAACCCCTACCATGGTACTGTATTGTGGTTATGCGCGTTCGAGGGGTACTTTAGCCCCCGGTTCGCAGAATATAAAAGTTAACGGGCTTCATCCGGATGAGCGAGCGTTTTGAAGTTGAAACATATCCACGAAGGAATGCACGCTCTCGGCTCCGATGGATTGCCTGCCAACAACTGAAAGGCTGACGTACAAGCTTTGGTTTCGTCCTAGGCCAAGAATTAATTATCTCAGATCGGTTTAGATTGGAAAGCTCGCGATGGCAAGCGTATTGGGGGGTTGAACAAAGTCACAACTTACAATTATTGTGGCTGGTATCGACACGGAATAACAGTCTCTTATAGGCCCCGGTGAATACAGAACGCAATTCGGTATGCTTTTGGCGTATTGTGACGCCCATCTGTCGAGCTTAGATATCCAAGGAGTTGCCAATTAGCACGAAAGCTTTCCGTCGGTGGCTCTATTATAGCACGACTTCAGTACCAAGGTCCAAGGTGCTGTTCATCTGGGTGGAGATGCCATAGATTCCAGAAACTCTAAAGTTTTCAGTGGAGACAGTCGGTATCAGGGTGTAAATATGTCCGGGGATAATCGAAATGGTACTCTTGACATTCAATTCGAGAATACTCTGACACGTCTCACGGATGACTTTCTCAATGGCATTCGAGAGCTCAAACCTGGACAACGCATGCATACCCGGATACATCACTAGGAAGCAACCTATCAATAGGGGAACACAGAATTTCGGTTAGTCATCCATTGAGGATTGAGTACTTCCAACGTCGCGACTTCGCACAACCACCTCAGGCTTTGAGTTTGCGCGGGGTCGCTGGTTCGTGGACTCGAACCCGCCCTTAATCTACTCAACTTCAAGGTGAGCATGAGTCGATGTGGGCTCCGCGGTGTAAAATGTCCATCGGGAGCTGTAGAACAACGATCACAGGAATTTGACAGCGGTGTGTGTCTCACCGCATCCACGGTTCCTTCCAGGAAGCGGTTGGTACCTCAGCACTTGTGTCCTAAACAACCCGGGACCGCCCTATTGTAGCTGTGGCCGGTGCCACCTCACATAGCTTCACCAGGTATCCGATCTATGCCGACGAGGCCGGCTGAGGCCCAACACGTCGTTGGCATCGGCGGGAATCAACCTGAAACCGGAGGTACTTCTGTTATGAAATTATCTCGGAGGGCCGGCTTGAACGGGCCCGGGTCCAGACGATCCATGATCCTATTCAGGCTAAGCCAAAATTATAGTTAGTGCCCTGTTCTAGTTGGCAGGCCATGCTCCTTACCCAAGCGCCGGGAACATCACTGGCCGAGCTACGATCGTAGAAGTACCCGTCACGAGCATCGTTGCTGCCTCCACACCCCTCGCAATTGTTGCTGGTGACCGCGGGCGTCATTGTTGCACAGGAATTTGTGATGGTCGAAATAACGCAGGCTCTTTCTTCGTCTAGCAAAGGGTAGGGCAAGATCTCCTAGGTGTCAACTACTGCAGTGTGTGCCTCCCGTGTTTTGCAGACATAATTCAGTATACTGTCCCAACCGTCCATGACTGCGATCACTCGTATAAATAGCCAAGCTCCCGAGACCAAAAGCTTCCGTTACCGTAGCTATGATGAGATACGTCTCAGAAGTGACTGCTGTAGTACGCTCACCTCAGCGGCTGAGCCTCAACAGACAAATGAGGCTTGCAGGGGTAGCAAATGAGGCTCCGCAAGTGCCCAACTACCTCTGTATTAGCGTTGTAGTGAACTTGCTTGATGGAACAATAGGTTCCAAGCCTGGGTACTGGATTGTAACTAAGAGGAGAACACCGTGTGGGAGACCCTCCTAATAGTTTTGCCCTTCACCCTTCACGCTTGTCATTGCAGCAGCGAGATATCCTACAGGATTGACGTGGTGTTGAATACAATATATAGTTCTACTACGCGAGAAAAACTCTTCATTCATAGTGATTCAATTAGCTTACGGTTGTGAACTTTGCGGTACCCTTATGAATCTAGAGCTGCTCTCTCACCATAAGCCCAGCTCGATTCTAGCAGATTATTGCAAGCTGATCCCCGTCCTCGGATATACACTACAGGTAAAGGTGTCGAGGCATTTTCGCAATCACTCGCCACTCCACCAGCCATAACGTACGTAAGATCCTCTTGCGGCCGAGGCATGGTGCCACAATACAGCGCAGACGGCGTCTACGCGCTACATTATGAAGACTCCACCCTGGGTTAAAGATTATTAAAGTGGTCGACCGATTCGAGCTTCTCAATCAAATTCTGAGCCCTAATCAGGCGTGACTGTACAATGGGTGAAACGGAGCCATCCGATCAGACTTCAGGAAATTTTCCTGTTATCCAGGGACTAAGGCCATACTCCCCCTGAAATGTGTCCAAACCCTGTAGTAGAGGGGGAAGTCTGGTGCTCGTATATTCTGCGTCACGCGCTTCATGCCAGGAAGTCACTAGTCTAGGCAGGATGTAGTCATCGCCTCAGACAGGTACTACTTGAGTGGTCAGAGAAAAATTCACGCAGATGGCTAAAATAGGAGTCCACAAATACTGTGCTTACGGCCATCAAATGAACGCCCTTCCGTTCAGTTCGTCGTACGACGTGTTATAGTTACCACTCGGCCATAAGTAGATGCAGCGTTGTGTTGATACGCTACGAAAAGAGTCAAGTTTATCCGTGCCCCGTCTAAGTTTGGAGGGAGTTCTTGGGAACGGTTGCTATAGGAGAAAGCGGTTCACACCCCTAGGTGGTCATCCGTTAGTCGCGGGTCAGAGGCGACCACCTCAGCGCAATTACGCTTGGGGCAGCCTGATAACAAACCGACTCTGGCAGCGGGCGTGGTCTTTAATTCGCCCAATAGCATCCGTTGTGGGAGCAGTCGAATTCGTAAGTTTGATCTCACTAACTCAAACCTCACATTGGCAACCAGATCGCAGCCGGAGCCGATGAATTTGAAGGGTTCTGTAAAAGTCGTCTGTGTTTGGTCGTTAAGGTGGGCCATGCGGGGGATGGTGCGTCCTGGATATAAGTCTACAGGCTTCCTGATAGAAGCCTTGGCTTTTTGCGTTCCGTAACTACCGCACCACTACCGAACAGTCAGCCAAGATACGGTCGACAGAACATTAGGGACACCCAAACGGACCCAATGGTATTCCCAAAAAGACATGAGTAGAGCATGCGAGCTTGCAGGCTGGTATCACCTTGCAACTCTGTACAAGTTTGCGATTATAGACATACTAGTACAAATCGCCGGACACTTTCGGTTTCCGCGACATTAGCCAGTCCTGATCTTTCGGATTTCATTGAACCTTGGCGGGAGTCCAGGAGCAATCCGTCCGTTCATCATGCCACAGTTTGCTTAAACAGTCCAGTCCCACAGATAATGAGGTCAAGCATCTCCCGTACAACGTCCTGCTGCGGACTTCGTCTGATTATTGTCCTCATCAGACGCCGGTTGAGGATTGTAGCCAGAGATAAATACCTTGTAAAGCTTATGGCCCCCTTGCCATGCATCTGACTAATAATTATGTCAGCAGGATTACGGCGAAACGGGAAGTTTTGCCCACGTTATCATGTACGGTGTGGCCACAGTCTGCCAATTGCGATGTATACCCTTTGGGCAGGAAAACCATTCGATATCTAGGGGAGTGCTAACTCCGTCTGACGATACGTCTCATCTGACTGAGGATTCCTACGCGCGTGATACTTAACGTAACAGTCAAAGGGTAGGGGGGGAAGACCATTCCGTATTTACTGTGCACCTGCAATTCGTAGGCCAGAAACTGGAAGGTACGTATGGACGTTTAGAGGATGTTTTACAGTTATCTAGACGCATGATCTTCCAAGTTAAGGAATTATGCGACAGAGTGTGAGCCGACGGTGGGGTCTAGTGGATCCTGCGAGTTGGGCAGTGGTCAACTTATGGCTCCAGAAGGCACCTACGCCCCGGATATGCTCCATGGGCCCATGCTTTGTGTGGTACAAACATGGCAATGTGTAGATAAACGTGAAGATGCATACAGGTGTGTCGGACGGACCCCTTCATAGCCGATGCTGGTAAGCAGTGACTGGCGAAGAGCGTCTGTATCTAATCCGCACAAAGGCATGCGCAGGTGATGCCCCTCGTCGCAAGTGACAAAGACGGAGGAATGCGAGGTTGAAGAGTTCGCCACCTCGACTAGTTTCGCCATATTTTTCACAGTTGCTTTCGGTTAGGCAGGGTACGTGGCTCTGGGAACCATTCCTTCTAGCTTTGCAGGACTACGTCTCTGTCGGACGATATATACCCGTCTTCAGCACCGGTATCGTGATGGATACTCATCGGGAACCCTTCTTTTGGTGAGCCGTCGGATTGGGAGGTCTAATGACAATAGCATCAGCACCGTACCGGGCGGTGCCGGCTCGAACTAATGGTGGCGCGGAGGTTTACCATACGTAGGAGTTTGAGCTCACTATTTAGCCGACGCTGCTCAATAGCGGCAATAGTTCGCCGACGATCCCGGGTCACTTTTACAGGCAAGTACCAGTAATTTGGGACTGTGGAGCCTTTCCGACACGGCAGTAGATGGTTATTCGGGATTAGTAACACCCCTTTGATCAGGGAAAAGCTGAGACACGTGAGGAAATTCCGAGGGTCTGTGTCTGTCAAAGGGTAAAGAGTATTGGTCACGGAGGGTGCAGTTCATAACGGACCGTTCCGGGGTCGTTAGCCCTGACTTAAGAACCTAGGAGCCTCGCCCCCCGTGTCTCAAAGCAAGTAGTTTGCCTACCTAGCACTGATTGTTGCGCTCCTCCCGCCAGTCGTAACCAACGCACTTTTTGTACGGACACCTCAAGACCGGTAAAGCCCACGAGACCTCCATATCGATTCTTCTGAATTACTGTACAATTGCTCCGCTTTGGCATTGCCGGACCGCTCAGGAGAAGGGTATGACGTTCTTTAGATTCGGTAAAACGAGAATAGGGCGGGACGCGACTGGTGAACGGACTTGACAATTGTACCCGTAATGGGGAACGTATTTGCCCTTGTCACCAGCAATTCCATGGGCTAACGTCCAAAAATCTCCCCTGTACGCACATCATACGGCGCCAACCTGTCCTGTTTATCGCTTGCTCTACGATGACTGTTCATGGCCGGAAGAAATAGCACTCCGCTAACGTGGTGCCGCCGAGGATTTCGTACTGCACTTCCAGTGTGTGGCCTCCACATAGCGTGCCACGCAATTCCCTGAGACCTATCCGCTTTTCAGGGGCTACATTCCTGGTGTACTGTAAATAATCCCCCAAATCCGGGTTATGCACGCCCGACGCGGCGCTACCGGTTAGGCTGGAAAGTCTGTCTAAATGGTTTCTTTGATAACTGCCGCAACAGCCCACTCGCGGCAGAATCGTACGAAGGCACATCTATCTAGCGTGTCTTAAGACCCCATGATTTGTGTCTGAAAACAGCGCACAATGAGGACGTGCGCATCCTCAATGTCAGCAGGGTCATGTCTCGTGCACCTATCAACGATCTACAATTAACTCACGACCTGGGAAAGATGGTAATTCTGGTCGATAGCGTCGGAAGGCGCTCATATCCGCTGGTTGGCCCGTGTGGTCGGCCGAGTGCTAAACGACCGATGGTGAAACGCCCCCACGCTGATACGCATCTGTGCTCAGGTCTGTCAGCGCGCGCCCGGGCTTCGCTGGACTCGTGGACAGTAGACAAAGCCGTATACAATTCTACGCCCACGACTTCTTATCCCACCGCAATACTGGTAAGTACGTTTCTAATGACCGTCCTAACCGGTGATCTTCGTCGTGCATGAGCTCGATGCCAGAATGATCCTTCGTAACCATAACGCCATGATCTGTTCTACCGTGCCAACGCGCCTTTCGGGACCTTCAATGCCTAGTGGATGTAAGACTAGGTCAGATTCACCATGCCCATGAGCGTGCTTATGGGGCTTTCATGCTCATTCTAGAGGATGTGTTAATGATTTGCGCACACGTGTACCCCCGGTGTGGCAGGGCAGGAGCTCATCGGCGGTCTACAAGGGCCGAAGCCATAGGATAGGTTACTGGCTTTTTCATGCGTTCTTGCTCCCCGGCATGTCCACACTGCTCCGGTGCTGTCGAGTGTGCTACGTTCGCTGATGGAGCCGAGATATTATACGATAACGCAGGGGATTTGGATCCACCTGTCCCAAGGTGGGCGGGTGTTTTAGGAGGCGCGGAGACCGTTTAAGATATATTGTTATTCGGTGTTACTCTCATGGTTCCGGCGGGCCGAAGGGCAGCTTACAGAAATCCGTTAGTACTTGTGCAGATCCTGCACGTCCATACCATCATGAGTGGGGGTGCACCAGCAGTGCTCCAGCAGCGTTCACCAAGGGGCCTACCGATTCCCCGACTGCACAAGCTATGATTACCATTTGCACGTGCACCGCGTGTCGATCTAAGGCGAGCGAGAAGAAGGACGCCGACATTAAAAAAGTGTAAACCCCGAATGGACCTCGAGAATGTCAATGTATCGAACGCTTCAAAGCCTTGTACAGTGTCATTTCTTTCCGTGCTGGCCTAGTCGTGCGAGTACGTGGGGGATCCGGATCTTGGTCCTGACACCCGTACATCGTGTAGCGACATCGAGTGACCAGTTCCATTACACAGGTCGATGCCCTCCCTTGTTGGGAAACCCCCCTCATGTAAACGGGAAGGTTGGAACAGCTCTATTTTGCTAGGATCATCTATTCTGGCAATTGGGACCATTCCAAACGCCTTGAGCCTATTAACAGGGCCATTACGAAGGACCTATCTTCACACCTATAACGTCCGTGCGTATATTTGGAGTTAGGGCTAGAAAATTGCTATATAGCCTTGTAGTTAGAGCTCATCGAGAGCCACCAGCTGAAAGACTCCCCCCGGGCGTGCCAACAAAGGTAGCTCCATTTGATATGGCCTCGTATTGCCCACTAGAGATGGCGCGCACTGGGTTCGCTACGAATATCGCTGCCAAAAGTTGCATCCTAGCCGACCTAGCGAATCGTAGGAAAGCTGCACTCAAAAATGTACTCTACAAAATCGGGGATGGACAACGTTGAATTACCTCGGCCCCGATCAGTCCGTACAATCTCGAGGAAAATGACCCGCAGTTCAGCCCGGACAACAATTGGCATCACTTGTGGAGATATGGGATCGTGGGCTTG')))