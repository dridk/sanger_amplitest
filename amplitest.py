
from abifpy import Trace
import begin

#==============================================================
def amplitude_from_abif(filename):
	''' f
	Return amplitude dictionnary for each base. 
	filename : sanger data abif format 
	seq      : compute amplitude only for a sub sequence 
	''' 
	abif   = Trace(filename)
	ampl   = abif.get_data("P1AM1")
	output = []

	index  = 0 
	end    = len(abif.seq)

	while index < end : 
		base  = abif.seq[index]
		output.append((base,abif.get_data("P1AM1")[index]))
		index+=1

	return output
#==============================================================


def run () : 
	fileA = amplitude_from_abif("data/A_forward.ab1")
	fileB = amplitude_from_abif("data/B_forward.ab1")

	seqA  = "".join([i[0] for i in fileA] )
	seqB  = "".join([i[0] for i in fileB] )

	beginA = seqA.index("TTTGATGCTGTCCCCGGACGATAT")
	beginB = seqB.index("TTTGATGCTGTCCCCGGACGATAT")

	endA = seqA.index("CTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTG")
	endB = seqB.index("CTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTG")



	fileA = fileA[beginA:endA]
	fileB = fileB[beginB:endB]

	seqA  = "".join([i[0] for i in fileA] )
	seqB  = "".join([i[0] for i in fileB] )

	# print(seqA.index("ATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGC"))

	# print(seqA[250:350])

	# print(seqB[250:350])
	

	for i in range(min(len(fileA), len(fileB))):
		bA     = fileA[i][0]
		bB     = fileB[i][0]

		ampliA = fileA[i][1]
		ampliB = fileB[i][1]


		print(bA, bB, ampliA-ampliB)



run()




# @begin.start 
# def run(filename):
# 	r = amplitude_from_abif(filename)
# 	for item in r : 
# 		print(item[0],"\t", item[1])








