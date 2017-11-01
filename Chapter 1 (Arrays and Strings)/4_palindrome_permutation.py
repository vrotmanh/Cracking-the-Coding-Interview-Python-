def is_palindrome_permutation(s):
	d = {}
	for i in s:
		if i in d:
			d.pop(i, None)
		else:
			d[i]=1

	return len(d)<=1

print(is_palindrome_permutation('lheehllol'), 'expected: True')
print(is_palindrome_permutation('hay'), 'expected: False')
print(is_palindrome_permutation('lheehllolaa'), 'expected: True')
print(is_palindrome_permutation('wowow'), 'expected: True')