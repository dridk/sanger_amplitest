
from abifpy import Trace


#==============================================================
def amplitude_from_abif(filename,seq):
	''' Return amplitude for each base ''' 
	abif  = Trace(filename)
	ampl  = abif.get_data("P1AM1")
	output = []
	index = abif.seq.find(seq)
	end   = index+len(seq)

	if index == -1 : 
		print("cannot find sequence")
		return
	
	while index < end : 
		base  = abif.seq[index]
		output.append((base,abif.get_data("P1AM1")[index]))
		index+=1

	return output
#==============================================================

def diff_amplitude(amplitudes):
	''' amplitudes are a lists a same size ''' 









r1 = amplitude_from_abif("data/A.ab1","CTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGA")
r2 = amplitude_from_abif("data/C.ab1","CTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGA")

a1 = [i[1] for i in r1] 
a2 = [i[1] for i in r2] 


print(a1)
print(a2)
