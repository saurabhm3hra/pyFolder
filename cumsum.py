def cumsum(l):
    for i in range(len(l)):
        for j in range(i):
            l[i]=str(int(l[i])+int(l[j]))

l1 = ['1','2','3','4','5']
print len(l1)
cumsum(l1)
print l1
