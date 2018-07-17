s=raw_input("enter string")
c=0
len1=len(s)
for i in range(len1-2):
	if s[i]=='b':
		if s[i+1]=='o':
			if s[i+2]=='b':
				c=c+1;
	
print("No. of times are ")
print(c)
