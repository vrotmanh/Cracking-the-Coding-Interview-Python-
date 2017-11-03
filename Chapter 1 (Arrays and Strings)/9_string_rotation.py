count = 0
bad = 0

def string_rotation(s1,s2):
	if(len(s1)==len(s2)):
		return s2 in (s1+s1)
	return False

def print_result(s1,s2,ex):
	global count
	global bad
	count+=1
	res = string_rotation(s1, s2)
	if res != ex:
		bad+=1
	print(s1,s2,'result: '+str(res), 'expected: '+str(ex))


print_result('waterbottle', 'erbottlewat', True)
print_result('hello', 'ohell', True)
print_result('hahahaha', 'hahahaha', True)
print_result('hello world', 'world', False)
print_result('wowoo', 'oowow', True)
print_result('yukjta,fch', 'erbottuyfjlewat', False)
print_result('hello. hello', '. hellohello', True)
print_result('hello. hello1', '. hellohello', False)
print("Total tests: "+ str(count), "Errors: " + str(bad))

