test=input("Enter string:")
l=[]
l=test.split()
wordfreq=[l.count(p) for p in l]
print(zip(l,wordfreq))
print(dict(zip(l,wordfreq)))