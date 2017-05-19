'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
'''

def file_to_list(file):
	with open(file, 'r') as f:
		data = f.read().replace('"', '')
		data = data.replace(',',' ')
		data = data.split()
    	return data

def alphabetize(list):
	i = 0
	while i < len(list):
		if i != 0 and list[i] < list[i - 1]:
			list[i], list[i - 1] = list[i - 1], list[i]
			i += -1
		else:
			i += 1
	return list

def word_value(word):
	sum = 0
	for a in word:
		sum += ord(a) - ord('A') + 1
	return sum

def list_total(list):
	sum = 0
	n = 1
	for e in list:
		sum += word_value(e) * n
		n += 1
	return sum

print list_total(alphabetize(file_to_list('p022_names.txt')))

