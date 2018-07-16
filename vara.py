varA=7
varB=5
#print(type(varA))
if isinstance(varA,str) or isinstance(varB,str):
	print("string involved")
elif varA>varB:
	print("bigger")
elif varA==varB:
	print("equal")
else:
	print("smaller")

