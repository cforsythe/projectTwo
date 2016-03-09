#http://pillow.readthedocs.org/en/3.1.x/handbook/tutorial.html
#http://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil 
#https://docs.python.org/2/tutorial/modules.html
#use a png
from PIL import Image
import functions
import copy

originalImage = Image.open("1.png")
pixel = originalImage.load()
width, height = originalImage.size

#originalImage.show()

wordsFromFile = functions.openFileReadText()
binaryListOfWords = functions.makeBinaryListOfWords(wordsFromFile)

listOfBitsToHide = []

for binaryWord in binaryListOfWords:
	for bit in binaryWord:
		listOfBitsToHide.append(bit)


functions.printList(listOfBitsToHide)
print  "number of bits to hide", len(listOfBitsToHide)
#This creates an integer value that will control the loop that creates a list of RGB values needed
if(len(listOfBitsToHide) % 3):
	numberOfPixelsNeeded = (len(listOfBitsToHide) / 3) + 1
else: 
	numberOfPixelsNeeded = len(listOfBitsToHide) / 3
print  "number of pixels needed", numberOfPixelsNeeded

numberOfRowsNeeded = (numberOfPixelsNeeded/width) + 1;
print  "number of rows needed", numberOfRowsNeeded

print "width", width
print "height", height

listOfRGBValues = []

counter = numberOfPixelsNeeded
#This loop creates a list of the RGB values needed
for y in range(0, numberOfRowsNeeded):
	for x in range(0, width):
		#if(x < width):print x
		#print x
		if(counter != 0):

			redValue, greenValue, blueValue = originalImage.getpixel((x, y))
			binaryRed = functions.makeNumberBinary(redValue)
			binaryGreen = functions.makeNumberBinary(greenValue)
			binaryBlue = functions.makeNumberBinary(blueValue)
			#print "red " + str(redValue) + " green " + str(greenValue) + " blue " + str(blueValue)
			listOfRGBValues.append(binaryRed)
			listOfRGBValues.append(binaryGreen)
			listOfRGBValues.append(binaryBlue)
			counter -= 1
		else:
			break

#print "RGB bit values unchanged"
#functions.printList(listOfRGBValues)


#print "bits will now be hidden"

binaryListOfHiddenTextInPixels = []
stringOfHiddenBits = ""

#For each iteration this loop creates a string of 8 bits bits 1-7 are from RGB values and bit 8 is the bit that needs to be hidden

for ix in range(0, len(listOfBitsToHide)):
	for jx in range (0, 7):
		stringOfHiddenBits += listOfRGBValues[ix][jx]
		
	stringOfHiddenBits += listOfBitsToHide[ix]
	binaryListOfHiddenTextInPixels.append(stringOfHiddenBits)
	stringOfHiddenBits = ""

#functions.printList(binaryListOfHiddenTextInPixels)

#This loops gets all decimal values of each binary string and creates 	a new list
listOfNewRGBValues = []
for ix in range(0, len(binaryListOfHiddenTextInPixels)):
	listOfNewRGBValues.append(functions.makeBinaryANumber(binaryListOfHiddenTextInPixels[ix]))

#functions.printList(listOfNewRGBValues)

img = Image.new( 'RGB', (width, height), "black") # create a new black image
pixels = img.load() # create the pixel map

#print "Number of Rows ", numberOfRowsNeeded
#print "Number of Pixels ", numberOfPixelsNeeded
otherCounter = numberOfPixelsNeeded
for y in range(0, numberOfRowsNeeded):
	for x in range(0, width):
		if(otherCounter != 0):
			pixels[x,y] = (255, 0, 0) # set the colour accordingly
			otherCounter -= 1

img.show()