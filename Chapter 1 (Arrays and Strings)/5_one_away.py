import unittest

def one_away(s1,s2):
	changeFound = False
	if abs(len(s1)-len(s2)) > 1:
		return False
	elif abs(len(s1)-len(s2)) == 1:
		l = len(s1) if len(s1)>len(s2) else len(s2)
		if l==1:
			return True
		j=0
		i=0
		while i < l and j < l:
			if s1[i] != s2[j]:
				if changeFound:
					return False
				changeFound = True
				if len(s1) > len(s2):
					j-=1
				else:
					i-=1
			if len(s1)==i+1 or len(s2)==j+1:
				return True
			j+=1
			i+=1

	else:
		j=0
		i=0
		while i < len(s1):
			if s1[i] != s2[j]:
				if changeFound:
					return False
				changeFound = True
			j+=1
			i+=1

	return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()