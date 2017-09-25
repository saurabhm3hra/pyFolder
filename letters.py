def letters(strg,dic):
	strg = strg.lower()
	for i in strg:
		dic[i] = dic.get(i,0) + 1

dic = {}
f = open("/usr/share/dict/words","r")
word_list = f.readlines()
for word in word_list:
	letters(word,dic)
dic_items = dic.items()
dic_items.sort()
print dic_items
