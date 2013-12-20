f = open("output.txt", "w")

def count(word, book):
	l = []
	for i in range(0, len(book) - len(word) + 1):
		if book[i:i+len(word)] == word:
			l.append(i)
	return l

def already_checked(pos, checked):
	for i in checked:
		for j in i:
			if pos == j:
				return True
	return False

def better_max(checked):
	done = [[0]]
	for i in checked:
		if len(i) > len(done[0]):
			done = [i]
		elif len(i) == len(done[0]):
			done.append(i)
	return done

def kmer(sequence, word_length):
	checked = []
	for i in range(0, len(sequence) - word_length + 1):
		if not already_checked(i, checked):
			checked.append(map(lambda x: x + i, count(sequence[i:i+word_length],sequence[i:])))
	indicies = better_max(checked)
	answer = []
	for k in indicies:
		answer.append(sequence[k[0]:k[0] + word_length])
	return answer


print kmer("AGTGATAAAATCATTTATAAGAGTTAGGAGTTAGGATATAAGAAGTGATATATCGTAGTATAAGATATAAGATATAAGATATCGTAGAAATCATTAAATCATTTATAAGATATCGTAGTATCGTAGTATAAGAGTTAGGAGTTAGGATATAAGAAGTGATAAAATCATTAGTGATAAAATCATTAGTGATAAGTGATAAAATCATTGTTAGGATATCGTAGTATCGTAGGTTAGGAGTTAGGAGTTAGGATATAAGATATCGTAGTATCGTAGAGTGATAAGTGATAAGTGATAGTTAGGAGTTAGGAAAATCATTAAATCATTTATCGTAGTATAAGAAAATCATTGTTAGGATATAAGAGTTAGGAAGTGATAAGTGATAGTTAGGAGTTAGGATATCGTAGAGTGATAGTTAGGAAGTGATAAAATCATTTATCGTAGGTTAGGATATAAGATATCGTAGTATCGTAGAAATCATTTATAAGAAGTGATATATCGTAGGTTAGGAAAATCATTAGTGATAGTTAGGAAGTGATAAGTGATAAAATCATTAGTGATAGTTAGGAGTTAGGAGTTAGGAGTTAGGATATCGTAGAAATCATTAAATCATTTATAAGAGTTAGGAAAATCATTAAATCATTAGTGATATATCGTAGAGTGATATATCGTAGTATAAGATATAAGATATCGTAGTATAAGAAAATCATTGTTAGGAAAATCATTAAATCATTAGTGATATATCGTAGTATAAGATATCGTAGAAATCATTTATAAGATATAAGATATAAGAGTTAGGAAAATCATTGTTAGGATATCGTAGAGTGATATATCGTAGAGTGATATATAAGATATCGTAGTATCGTAGAAATCATTTATAAGA", 14)