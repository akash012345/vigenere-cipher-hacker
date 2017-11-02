# vigere cipher freq analysis hacker

import freq_analysis,time

n=5

count=0

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_strings(message):

	strings=['']*n

	k=0;

	for i in message:
		if i in LETTERS:

			strings[k] += i
			k+=1
			k=k%n
	return strings


def find_key(stri):

	score=[]
	max_score=0
	sec_max_score=0
	let=[]
	sec=[]
	for i in LETTERS:
		#print(str(i)+ ' : '+str(decrypt(stri,i)))
		score.append(decrypt(stri,i))

	temp=score
	max_score=max(temp)
	for i in range(26):
		if score[i]==max_score:
			let.append(LETTERS[i])
			score[i]=0
			

	print(let)
	return let


def decrypt(message,i):
	global count;

	count+=1

	key=LETTERS.find(i)
	translator=''
	for symbol in message:
		if symbol in LETTERS:
			num=LETTERS.find(symbol)
			num=num-key
			num=num%26
			translator=translator+LETTERS[num]
		else:
			translator=translator+symbol

	return freq_analysis.freq_match(translator)


def find_subkeys(message):

	strings=make_strings(message)

	keys=[]

	for i in strings:
		keys.append(find_key(i))

	#find_key(strings[0])
	return keys


def main():

	f=open('encrypted_text.txt')
	message=f.read()
	f.close()
	#message=message.upper()

	message=message[:2000]
	#message='''PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'''
	#print(find_subkeys(message))
	find_subkeys(message.upper())
	print(count)

def time_tester(lim):
	startTime=time.time()
	f=open('encrypted_text.txt')
	message=f.read()
	f.close()
	#message=message.upper()

	message=message[:lim]
	#message='''PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'''
	#print(find_subkeys(message))
	find_subkeys(message.upper())
	print(count)
	endTime=time.time()
	timeTaken=round(endTime-startTime,3)
	print(timeTaken)


if __name__=='__main__':
    main()