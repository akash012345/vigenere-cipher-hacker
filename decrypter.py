#vigenere cipher decrypter


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():

	f = open('encrypted_text.txt')

	myMessage = f.read()

	myKey='AAAAZ'

	translated = decryptMessage(myKey,myMessage)

	q = open('decrypted_text.txt','w')

	q.write(translated)

	f.close()
	q.close()


def decryptMessage(myKey,myMessage):

	translated=[]

	myKey=myKey.upper()

	key_num=0;

	for symbol in myMessage:

		num= LETTERS.find(symbol.upper())

		if num != -1:

			num=num - LETTERS.find(myKey[key_num])

			key_num=key_num+1

			num = num%len(LETTERS)

			key_num=key_num%(len(myKey))

			if symbol.isupper():

				translated.append(LETTERS[num])

			elif symbol.islower():

				translated.append(LETTERS[num].lower())


		else:
			translated.append(symbol)

	return ''.join(translated)

main()
