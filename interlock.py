import bisect
def interlock(word_list):
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            new_word = ''
            if(len(word_list[i])==len(word_list[j])):
#                print word_list[i] + " / " + word_list[j]
                for k in range(len(word_list[i])):
                    new_word = new_word + word_list[i][k] + word_list[j][k]
                tf = bisect.bisect_left(word_list, new_word)
                if word_list[tf] == new_word:
                    print word_list[i] + " / " + word_list[j] + " = " + new_word


fin = open('words.txt')
word_list_n = []
for line in fin:
    word = line.strip()
    word_list_n.append(word)
#print word_list_n
interlock(word_list_n)
