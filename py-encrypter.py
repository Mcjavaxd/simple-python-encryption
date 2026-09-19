#created pool using gemini AI
import random
ENCRYPTION_KEY = {
    # Uppercase
    'A': 'k', 'B': '8', 'C': 'z', 'D': 'Q', 'E': '3', 'F': 'm', 'G': 'T',
    'H': '9', 'I': 'v', 'J': 'B', 'K': 'l', 'L': 'o', 'M': 'F', 'N': '1',
    'O': 'P', 'P': 'x', 'Q': 'R', 'R': 'H', 'S': '0', 'T': 'W', 'U': 'c',
    'V': 'a', 'W': 's', 'X': '6', 'Y': 'N', 'Z': 'J',
    
    # Lowercase
    'a': 'U', 'b': '5', 'c': 'L', 'd': 'i', 'e': 'D', 'f': 'O', 'g': 'y',
    'h': 'G', 'i': 'K', 'j': '4', 'k': 'r', 'l': 'V', 'm': 't', 'n': 'X',
    'o': 'M', 'p': 'w', 'q': 'd', 'r': 'I', 's': 'b', 't': 'q', 'u': 'A',
    'v': 'n', 'w': 'C', 'x': 'h', 'y': 'p', 'z': 'E',
    
    # Digits
    '0': '7', '1': 'S', '2': 'e', '3': 'g', '4': 'u', '5': '2', '6': 'Z',
    '7': 'f', '8': 'Y', '9': 'j'
}

DECRYPTION_KEY = {
    # Inverted from Uppercase
    'k': 'A', '8': 'B', 'z': 'C', 'Q': 'D', '3': 'E', 'm': 'F', 'T': 'G',
    '9': 'H', 'v': 'I', 'B': 'J', 'l': 'K', 'o': 'L', 'F': 'M', '1': 'N',
    'P': 'O', 'x': 'P', 'R': 'Q', 'H': 'R', '0': 'S', 'W': 'T', 'c': 'U',
    'a': 'V', 's': 'W', '6': 'X', 'N': 'Y', 'J': 'Z',

    # Inverted from Lowercase
    'U': 'a', '5': 'b', 'L': 'c', 'i': 'd', 'D': 'e', 'O': 'f', 'y': 'g',
    'G': 'h', 'K': 'i', '4': 'j', 'r': 'k', 'V': 'l', 't': 'm', 'X': 'n',
    'M': 'o', 'w': 'p', 'd': 'q', 'I': 'r', 'b': 's', 'q': 't', 'A': 'u',
    'n': 'v', 'C': 'w', 'h': 'x', 'p': 'y', 'E': 'z',

    # Inverted from Digits & Space
    '7': '0', 'S': '1', 'e': '2', 'g': '3', 'u': '4', '2': '5', 'Z': '6',
    'f': '7', 'Y': '8', 'j': '9',
}


spacebar=['!','@','#',"$",'%',"^"]

#MAIN ENCRYPTION
def encrypt():
	print()
	a=input("Enter your file name: ")

	#File opening
	f=open(a,'r')
	data=f.read()
	f.close()

	#Data extraction
	line=data.split('\n')
	data_new=[]
	for i in line:
		line1=''
		for x in i:
			if x==' ':
				new_letter=random.choice(spacebar)
			elif x in ENCRYPTION_KEY:
				new_letter=ENCRYPTION_KEY[x]
			else:
				new_letter=x
			line1+=new_letter
		data_new.append(line1)

	#Encrypted file creation
	f=open(a,'w')
	for i in data_new:
		f.write(i+'\n')
	f.close()




#MAIN DECRYPTION
def decrypt():
	print()
	a=input("Enter your file name: ")
	f=open(a,'r')
	data=f.read()
	f.close()
	line=data.split('\n')
	de=[]
	for i in line:
		line2=''
		for x in i:
			if x in spacebar:
				new_letter=' '
			elif x in DECRYPTION_KEY:
				new_letter=DECRYPTION_KEY[x]
			else:
				new_letter=x
			line2+=new_letter
		de.append(line2)
	
	#Decrypted file creation
	f=open(a,'w')
	for i in de:
		f.write(i+'\n')
	f.close()





def main():
	print('========================')
	print('Simple Python Encryption')
	print('========================')
	print()
	print('1.Encrypt file')
	print("2.Decrypt file")
	print()
	a=int(input('Enter your option: '))
	if a==1:
		encrypt()
	elif a==2:
		decrypt()
	else:
		print('Enter your choice correctly')
main()

