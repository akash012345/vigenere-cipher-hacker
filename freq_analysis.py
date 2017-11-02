#frequency analysis

key_len = 5

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def getLetterCount(message):
	letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

	for letter in message.upper():
		if letter in LETTERS:
			letterCount[letter] += 1
	return letterCount

def getFrequencyOrder(message):
	letterCount=getLetterCount(message)

	freq=[None]*26

	for letter in letterCount:
		ind=LETTERS.find(letter)
		freq[ind]=letterCount[letter]

	ret_str=''

	for i in range(26):
		max_val=max(freq)
		ind=freq.index(max_val)
		ret_str += LETTERS[ind]
		freq[ind]=0

	return ret_str


def freq_match(message):

	freq = getFrequencyOrder(message)

	matchpoint=0

	for commonLetter in ETAOIN[:6]:
		if commonLetter in freq[:6]:
			matchpoint += 1



	for uncommonLetter in ETAOIN[-6:]:
		if uncommonLetter in freq[-6:]:
			matchpoint += 1

	return matchpoint


def main():
	f=open('input')
	content=f.read()
	print(freq_match(content))


