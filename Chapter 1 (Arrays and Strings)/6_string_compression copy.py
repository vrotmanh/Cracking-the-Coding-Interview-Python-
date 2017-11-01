def string_compression(s):
	if len(s)<2:
		return s
	comp = ''
	i = 0
	while i<len(s):
		comp+=s[i]
		count = 1
		loop = False
		while i+1<len(s) and s[i] == s[i+1]:
			loop = True
			count+=1
			i+=1
			if i+1 == len(s):
				break
		if loop:
			comp+=str(count)
		i+=1
	if len(comp)<len(s):
		return comp
	else:
		return s

#Github solution (THIS SOLUTION PUT 1 AFTER CHARACTER THAT APPEARS ONLY ONE TIME, THE SOLUTION ABOVE DOESN'T)
def string_compression2(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, ''.join(compressed), key=len)


print(string_compression('heeelo'), 'expected: he3lo')
print(string_compression('heeeloo'), 'expected: he3lo2')
print(string_compression('hheeaa'), 'expected: hheeaa')
print(string_compression('aabcccccaaa'), 'expected: a2bc5a3')
print(string_compression('abcdef'), 'expected: abcdef')

# len = 6
# comp = he3l
# count = 1
# i = 5
# s[i] = l
# s[i+1] = o