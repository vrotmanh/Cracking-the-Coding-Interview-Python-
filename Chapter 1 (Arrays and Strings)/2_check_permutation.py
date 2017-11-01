# First solution O(n)
def is_permutation(s1, s2):
	return generate_dict(s1) == generate_dict(s2)

def generate_dict(s):
	d = {}
	for i in s:
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	return d


# Elegant solution (n log(n))
def is_permutation2(s1, s2):
	return sorted(s1) == sorted(s2)