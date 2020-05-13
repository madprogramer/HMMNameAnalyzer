import numpy as np
from hmmlearn import hmm
import pickle

#My Dataset is a secret to everyone 
def vowelOrConsonant(string):
	K = []
	for s in string:
		if s in ["a","e" ,"i" ,"ı" ,"o" ,"ö" ,"u" ,"ü" ,"A" ,"E" ,"İ" ,"I" ,"O" ,"Ö" ,"U" ,"ü"]: 
			K.append([0])
		else:
			K.append([1])
	return K

#Load
M = {}
with open("turkishModels.pkl", "rb") as F: 
	M = pickle.load(F)

MALEMODEL, FEMALEMODEL, SURMODEL = M["MALEMODEL"], M["FEMALEMODEL"], M["SURMODEL"]

# Model View

# print(MALEMODEL)
# print(MALEMODEL.startprob_)
# print(MALEMODEL.transmat_)
# print(MALEMODEL.emissionprob_)

# print(FEMALEMODEL)
# print(FEMALEMODEL.startprob_)
# print(FEMALEMODEL.transmat_)
# print(FEMALEMODEL.emissionprob_)

# print(SURMODEL)
# print(SURMODEL.startprob_)
# print(SURMODEL.transmat_)
# print(SURMODEL.emissionprob_)

# Rules
# Name + ... + Surname
# Name + ... + Surname + Surname

# Tests 
Tests = ["Barış Manço","Firuze Gül"]

for t in range(len(Tests)):
	print("Testing name {}:".format(Tests[t]))
	rawnames = Tests[t].split()
	names = (list(map(vowelOrConsonant,rawnames)))

	if len(names) == 1:
		MALE = MALEMODEL.score(names[-1])
		FEMALE = FEMALEMODEL.score(names[-1])
		print("Male: Female:")
		print(MALE, FEMALE)

	MALE = sum(list(map(MALEMODEL.score,names[:-1]))) + SURMODEL.score(names[-1])
	FEMALE = sum(list(map(FEMALEMODEL.score,names[:-1]))) + SURMODEL.score(names[-1])

	if len(names) > 2:
		MALE2 = sum(list(map(MALEMODEL.score,names[:-2]))) + sum(list(map(SURMODEL.score,names[-2:])))
		FEMALE2 = sum(list(map(FEMALEMODEL.score,names[:-2]))) + sum(list(map(SURMODEL.score,names[-2:])))
		print("Male: Female:")
		print(MALE,FEMALE,MALE2,FEMALE2)
	else:
		print("Male: Female:")
		print(MALE,FEMALE)








