str=raw_input("Enter string:")
vow=0
for i in str:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vow=vow+1
print("Number of vowels are:")
print(vow)
e= str.count('')
print("total",e)
g=e-vow
print("constant",g)
