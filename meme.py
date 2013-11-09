


def score(s1, s2):
	score = 0
	if s1[0] != s1[0]:
		return 0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			score = score + 1
	return 1. * score / len(s1)


def meme(s1, s2, s3):
	initial_best = ["", 0]
	final_best = ["", 0]
	for i in range(len(s1) - 20 + 1):


		for j in range(len(s2) - 20 + 1):
			current_score = score(s1[i:i + 20], s2[j:j+ 20])
			if current_score > initial_best[1]:
				initial_best = [s1[i:i + 20], current_score]

		for k in range(len(s3) - 20 + 1):
			if score(s1[i:i + 20], s3[j:j+ 20]) >= initial_best[1]:
				final_best = [s1[i:i + 20], score(s1[i:i + 20], s2[j:j+ 20])] # should take min of scores here
		initial_best = ["", 0]
	return final_best


def sim_meme(s1,s2):
	s1_done = False
	current_length = 20
	current_pos = 0 # establish parameters to keep track of s1 candidate
	current_score = 0.
	current_ans = ""
	ans_length = 0  # establish parameters for 


	while s1_done != True:
		current_frame = s1[current_pos: current_pos + current_length]
		s2_done = False
		s2_pos = 0
		while s2_done == False:

			s2_frame = s2[s2_pos: s2_pos + current_length]
			if score(current_frame, s2_frame) > current_score and score(current_frame, s2_frame) != 1.:
				current_score = score(current_frame, s2_frame)
				current_ans = current_frame
				ans_length = current_length
			if s2_frame == s2[-1 * current_length - 1:-1]:
				s2_done = True
			else:
				s2_pos = s2_pos + 1



		if current_frame == s1[-21:-1]:
				s1_done = True
		elif len(current_frame) > len(s1)/2:
			current_length = 20
			current_pos = current_pos + 1
		elif current_pos + current_length == len(s1):
			current_length = 20
			current_pos = current_pos + 1
		else:
			current_length = current_length + 1
		if current_score > .97:
			return current_ans

	return current_ans


#print score("DLWWCWIPVHKKPHSFLKTWSPAAGHRGWQFDHNFF", "DLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFF")

mah_answer = sim_meme("PFTADSMDTSNMAQCRVEDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFVYMMGQFYMTKYNHGYAPARRKRFMCQTFFILTFMHFCFRRAHSMVEWCPLTTVSQFDCTPCAIFEWGFMMEFPCFRKQMHHQSYPPQNGLMNFNMTISWYQMKRQHICHMWAEVGILPVPMPFNMSYQIWEKGMSMGCENNQKDNEVMIMCWTSDIKKDGPEIWWMYNLPHYLTATRIGLRLALY", "VPHRVNREGFPVLDNTFHEQEHWWKEMHVYLDALCHCPEYLDGEKVYFNLYKQQISCERYPIDHPSQEIGFGGKQHFTRTEFHTFKADWTWFWCEPTMQAQEIKIFDEQGTSKLRYWADFQRMCEVPSGGCVGFEDSQYYENQWQREEYQCGRIKSFNKQYEHDLWWCWIPVHKKPHSFLKTWSPAAGHRGWQFDHNFFSTKCSCIMSNCCQPPQQCGQYLTSVCWCCPEYEYVTKREEM")

#print score("DLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFF","DLWWCWIPVHKKPHSFLKTWSPAAGHRGWQFDHNFF")


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

print real_answer(mah_answer, "VPHRVNREGFPVLDNTFHEQEHWWKEMHVYLDALCHCPEYLDGEKVYFNLYKQQISCERYPIDHPSQEIGFGGKQHFTRTEFHTFKADWTWFWCEPTMQAQEIKIFDEQGTSKLRYWADFQRMCEVPSGGCVGFEDSQYYENQWQREEYQCGRIKSFNKQYEHDLWWCWIPVHKKPHSFLKTWSPAAGHRGWQFDHNFFSTKCSCIMSNCCQPPQQCGQYLTSVCWCCPEYEYVTKREEM", "ETCYVSQLAYCRGPLLMNDGGYGPLLMNDGGYTISWYQAEEAFPLRWIFMMFWIDGHSCFNKESPMLVTQHALRGNFWDMDTCFMPNTLNQLPVRIVEFAKELIKKEFCMNWICAPDPMAGNSQFIHCKNCFHNCFRQVGMDLWWCWIPVHKNPHSFLKTWSPAAGHRGWQFDHNFFQMMGHQDWGTQTFSCMHWVGWMGWVDCNYDARAHPEFYTIREYADITWYSDTSSNFRGRIGQN")