def cartalk(a):
    if(len(a)>4):
        i=0;
        while i < len(a)-5:
            if(a[i]==a[i+1]):
                if(a[i+2]==a[i+3]):
                    if(a[i+4]==a[i+5]):
                        print a
            i=i+1

fin = open('words.txt')

for line in fin:
    word = line.strip()
    cartalk(word)
