f = open('output.txt', 'w')

def pat_mat(pat, s):
	ans = ""
	for i in range(len(s) - len(pat) + 1):
		if pat == s[i:i+len(pat)]:
			ans = ans + str(i) + " "
	return ans

f.write(pat_mat('CTTGATCAT', ''))