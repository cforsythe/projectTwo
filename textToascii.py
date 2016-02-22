#https://docs.python.org/2/tutorial/inputoutput.html
#https://docs.python.org/2/library/functions.html
#https://docs.python.org/2/library/stdtypes.html
#use ord() to get ascii value
#http://www.greenteapress.com/thinkpython/thinkpython.pdf 

#This function accepts an ASCII value and returns the binary string of that ASCII value
def convertOneASCIIValueToBinary(lettersASCIIValue):
	binaryString = ""
	baseTwoValues = [128, 64, 32, 16, 8, 4, 2, 1] 
	for ix in range(0, 8):
			if(lettersASCIIValue < baseTwoValues[ix]):
				binaryString += "0"
			else:
				binaryString += "1"
				lettersASCIIValue -= baseTwoValues[ix]
	return binaryString

def openFileReadTextAndMakeBinaryString():
	fileWithText = open('words.txt', 'r')
	listOfWords = [] #Contains every word in text file
	fileContent = fileWithText.read()
	listOfWords = fileContent.split()
	oneWordInBinary = ""

	for ix in range(0, len(listOfWords)):
		word = listOfWords[ix]
		for jx in range(0, len(word)):
			oneWordInBinary += convertOneASCIIValueToBinary(ord(word[jx]))
		print oneWordInBinary
		print "End of word"
		oneWordInBinary = "" #clears the varible for next word in binary

openFileReadTextAndMakeBinaryString()
