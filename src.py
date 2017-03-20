strand = "atcctctcggactcctcaagtttgagctaagccaatcgaccccaaaggaagaggtaacgtcgcgtgcgagaggcaccgagtcctcctgggatgttagtt"

def transcription(seq):
		DNA = list(seq) #insert seq here for strand instead to use as a normal function
		for index in range (len(DNA)):
			if DNA[index] == "a":
				DNA[index] = "u"
				
			elif DNA[index] == "t":
				DNA[index] = "a"
				
			elif DNA[index] == "c":
				DNA[index] = "g"
				
			elif DNA[index] == "g":
				DNA[index] = "c"

		return DNA

RNA = (transcription(strand))
RNAString = "".join(RNA) #convert RNA back to string
print RNAString

codons = [RNAString[x:x+3] for x in xrange(0, len(RNAString), 3)]  #break up the transcribed strand into codons (this makes a list)
print codons 

proteins = {
	'uuu': 'phe', 
	'uuc': 'phe', 
	'uua': 'leu',
	'uug': 'leu',
	'ucu': 'ser', 
	'ucc': 'ser', 
	'uca': 'ser',
	'ucg': 'ser',
	'uau': 'tyr', 
	'uac': 'try', 
	'uaa': 'STOP',
	'uag': 'STOP',	
	'ugu': 'cys', 
	'ugc': 'cys', 
	'uga': 'STOP',
	'ugg': 'trp',	
	'cuu': 'leu', 
	'cuc': 'leu', 
	'cua': 'leu',
	'cug': 'leu',
	'ccu': 'pro', 
	'ccc': 'pro', 
	'cca': 'pro',
	'ccg': 'pro',
	'cau': 'his', 
	'cac': 'his', 
	'caa': 'gln',
	'cag': 'gln',
	'cgu': 'arg', 
	'cgc': 'arg', 
	'cga': 'arg',
	'cgg': 'arg',
	'auu': 'lle', 
	'auc': 'lle', 
	'aua': 'lle',
	'aug': 'met',
	'acu': 'thr', 
	'acc': 'thr', 
	'aca': 'thr',
	'acg': 'thr',
	'aau': 'asn', 
	'aac': 'asn', 
	'aaa': 'lys',
	'aag': 'lys',
	'agu': 'ser', 
	'agc': 'ser', 
	'aga': 'arg',
	'agg': 'arg',
	'guu': 'val', 
	'guc': 'val', 
	'gua': 'val',
	'gug': 'val',
	'gcu': 'ala', 
	'gcc': 'ala', 
	'gca': 'ala',
	'gcg': 'ala',
	'gau': 'asp', 
	'gac': 'asp', 
	'gaa': 'glu',
	'gag': 'glu',
	'ggu': 'gly', 
	'ggc': 'gly', 
	'gga': 'gly',
	'ggg': 'gly',
	}

def translation(seq):
	for i, val in enumerate(seq):
		if val in proteins:
			protein = proteins.get(val)
			print protein

translation(codons)
