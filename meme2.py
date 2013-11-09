s1 = "PFTADSMDTSNMAQCRVEDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFVYMMGQFYMTKYNHGYAPARRKRFMCQTFFILTFMHFCFRRAHSMVEWCPLTTVSQFDCTPCAIFEWGFMMEFPCFRKQMHHQSYPPQNGLMNFNMTISWYQMKRQHICHMWAEVGILPVPMPFNMSYQIWEKGMSMGCENNQKDNEVMIMCWTSDIKKDGPEIWWMYNLPHYLTATRIGLRLALY"
s2 = "VPHRVNREGFPVLDNTFHEQEHWWKEMHVYLDALCHCPEYLDGEKVYFNLYKQQISCERYPIDHPSQEIGFGGKQHFTRTEFHTFKADWTWFWCEPTMQAQEIKIFDEQGTSKLRYWADFQRMCEVPSGGCVGFEDSQYYENQWQREEYQCGRIKSFNKQYEHDLWWCWIPVHKKPHSFLKTWSPAAGHRGWQFDHNFFSTKCSCIMSNCCQPPQQCGQYLTSVCWCCPEYEYVTKREEM"
s3 = "ETCYVSQLAYCRGPLLMNDGGYGPLLMNDGGYTISWYQAEEAFPLRWIFMMFWIDGHSCFNKESPMLVTQHALRGNFWDMDTCFMPNTLNQLPVRIVEFAKELIKKEFCMNWICAPDPMAGNSQFIHCKNCFHNCFRQVGMDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFQMMGHQDWGTQTFSCMHWVGWMGWVDCNYDARAHPEFYTIREYADITWYSDTSSNFRGRIGQN"
def find_matches(s1,s2,s3, seed):
	ls = []
	i = 0
	while i < len(s1) - seed + 1:
		s2_find = s2.find(s1[i:i+seed])
		s3_find = s3.find(s1[i:i+seed])
		if s2_find != -1 or s3_find != -1:
			ls.append(i)
			ls.append([])
			if s2_find != -1:
				ls[-1].append(s2_find)
			else:
				ls[-1].append(-1)
			if s3_find != -1:
				ls[-1].append(s3_find)
			else:
				ls[-1].append(-1)
		i = i + 1

	return ls

# def give_bracket(a, ls):
# 	if len(ls) == 2:
# 		return a:
# 	else:
# 		brack = "[" + a
# 		if a !=

# def consolodate_ls(ls, s1, s2, s3):
# 	candidate_string = ""
# 	final_ans = ""
# 	for i in range(len(ls)):
# 		if isinstance(ls[i], int):
# 			print i
# 			candidate_string = give_bracket(s1[i], s2[ls[i+1][0]], s3[ls[i+1][1]])
# 			if i + 1 not in ls and i+1 in ls:
# 				candidate_string = give_bracket(s1[i+1], s2[ls[i+2][0]], s3[ls[i+2][1]])
# 		elif i + 1 not in ls:
# 			if len(candidate_string) > final_ans:
# 				final_ans = candidate_string
# 				candidate_string = ""
# 		else:
# 			candidate_string = ""
# 	return final_ans





def find_longest_runs(ls):
	candidate = [ls[0]]
	total = []
	for i in range(1, len(ls)):
		if isinstance(ls[i],int) and ls[i] - 1 == candidate[-1]:
			candidate.append(ls[i])
		elif isinstance(ls[i],int) and ls[i] - 1 != candidate[-1]:
			total.append(candidate)
			candidate = ['hello']

	return total

def score(s1, s2):
	score = 0
	if s1[0] != s1[0]:
		return 0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			score = score + 1
	return 1. * score / len(s1)

def real_answer(match_this, s2,s3):
	s2_best = ""
	s2_score = 0
	for i in range(len(s2) - len(match_this) + 1):
		if score(match_this, s2[i:i+len(match_this)]) > s2_score:
			s2_best = s2[i:i+len(match_this)]
			s2_score = score(match_this, s2[i:i+len(match_this)])
	s3_score = 0
	s3_best = ""
	for i in range(len(s3) - len(match_this) + 1):
		if score(match_this, s3[i:i+len(match_this)]) > s3_score:
			s3_best = s3[i:i+len(match_this)]
			s3_score = score(match_this, s3[i:i+len(match_this)])

	final_ans = ""
	for i in range(len(match_this)):
		if match_this[i] == s2_best[i] and match_this[i] == s3_best[i]:
			final_ans = final_ans + match_this[i]
		else:
			inter = "["
			inter = inter + match_this[i]
			if s2_best[i] != match_this[i]:
				inter = inter + s2_best[i]
			if s3_best[i] != match_this[i] and s3_best[i] != s2_best[i]:
				inter = inter + s3_best[i]
			inter = inter + "]"
			final_ans = final_ans + inter
	return final_ans

concentrations = find_longest_runs(find_matches(s1,s2,s3,5))

#print find_matches(s1,s2,s3,5)

print real_answer(s1[concentrations[0][0]: concentrations[0][-1]], s2, s3)

