
def generateBooks():
	f = open('static/isbns.txt','r')

	for line in f:
		book = line[0:line.index(' ')]
		b = open('static/Books/'+book+'.epub', 'a')
		b.write(book+' For full copy Pay the iron price')

if __name__ == '__main__':
	main()