DNAStrand = 'aaagtacctctcggactcctcaagtttgagctaagccaatcgaccccaaaggaagaggtaacgtcgcgtgcgagaggcaccgagtcctcctgggatgttagttattaaatgcctga'

def transcription(seq):
		DNA = list(seq) #insert seq here for strand instead to use as a normal function. 
		RNA = []

		for index in range (len(DNA)): #Switches out the DNA nucleotide for an RNA one.
			
			if DNA[index] == "a":
				RNA.append("u")
				
			elif DNA[index] == "t":
				RNA.append("a")
				
			elif DNA[index] == "c":
				RNA.append("g")
				
			elif DNA[index] == "g":
				RNA.append("c")

		return RNA #This returns a list of RNA nucleotides

RNA = transcription(DNAStrand) 

RawRNAString = "".join(RNA) #convert RNA from list back to string

print '\n' #Line break
print 'Raw RNA String:', RawRNAString

def substring_after(s, delim):
    return s.partition(delim)[2]

RNAString = substring_after(RawRNAString, 'aug') #Gets the entire string after the start codon (deletes the MET codon)

#print 'RNA String Without Start:',RNAString 

RNAcodons = [RNAString[x:x+3] for x in xrange(0, len(RNAString), 3)]  #Break up the transcribed strand into codons (this makes a list of groups of 3)

RNAcodons.insert(0,'aug') #Add the AUG codon back to position 0. 

#print 'List Of Codons With Start:',RNAcodons

def substring_before(s): #Function to get the list before the stop codon (deletes the stop codon-uaa, uag, or uga)
	FullRNACodons = []

	if 'uaa' in s: 
		x = s.index('uaa') #Define position of UAA stop codon as x
	else: 
		x = 0

	if 'uag' in s:
		y = s.index('uag') #Define position of UAA stop codon as y
	else: 
		y = 0

	if 'uga' in s:
		z = s.index('uga') #Define position of UAA stop codon as z
	else: 
		z = 0

	if x != 0: 
		FullRNACodons = s[:x] #Take the list before the position of the stop codon
		FullRNACodons.append('uaa') #Add back the stop codon

	if y != 0:
		FullRNACodons = s[:y]
		FullRNACodons.append('uag')

	if z != 0:
		FullRNACodons = s[:z]
		FullRNACodons.append('uga') 

	return FullRNACodons 

FullRNACodons = substring_before(RNAcodons)

print '\n' #Line break
print 'List Of RNA Codons in Correct Reading Frame:',FullRNACodons

proteins = { #This is a dictionary of RNA codons and their corresponding proteins
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
	proteinlist = [] #Create an empty list

	for i, val in enumerate(seq): #Go through all the RNA codons in the list 
		if val in proteins: #If the codon is a key in the dict
			protein = proteins.get(val) #Get the definition for the key (a protein)
			
			proteinlist.append(protein) #Add the proten to proteinlsit

	return proteinlist


proteinlist = translation(FullRNACodons)

print '\n'
print 'List of Protein Codons:',proteinlist
