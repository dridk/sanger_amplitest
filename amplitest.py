
from abifpy import Trace
import begin

#==============================================================
def amplitude_from_abif(filename):
	''' 
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


@begin.start 
def run(filename):
	r = amplitude_from_abif(filename)
	for item in r : 
		print(item[0],"\t", item[1])








