# Elegant Solution
def URLify(url):
	return url.replace(' ', '%20')

#Honest Solution
def URLify2(s):
	url=s.split()
	for i in range(len(url)):
		if url[i]==' ':
			url[i]='%20'
	return '%20'.join(url)

print(URLify2('Welcome to the world of Python'))
	