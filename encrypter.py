#vigenere cipher encrypter

#length of the text is 55334


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	myKey = 'aaaaz'



	f = open('plain_text.txt')

	myMessage = f.read()


	translated = encryptMessage(myKey, myMessage) 

	q = open('encrypted_text.txt','w')

	q.write(translated)

	f.close()

	q.close()

def encryptMessage(myKey,myMessage):

	myKey = myKey.upper()

	key_num = 0

	translated=[]

	for symbol in myMessage:

		num = LETTERS.find(symbol.upper())

		if num != -1:

			num = num + LETTERS.find(myKey[key_num])

			num = num%len(LETTERS)

			
			key_num=key_num+1
			key_num=key_num%len(myKey)

			if symbol.isupper():

				translated.append(LETTERS[num])

			elif symbol.islower():

				translated.append(LETTERS[num].lower())

		else:
			translated.append(symbol)


	return ''.join(translated)


main()

