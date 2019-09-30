
import time
import string
import sys
import os



clear = lambda:os.system('clear')
wincls = lambda:os.system('cls')

osname = os.name


class Main():
	def __init__(self):
		self.banner()
		time.sleep(1) #1.5

		self.decision()
		



	def banner(self):
		print('''\033[1;32;48m
                                       _       _               
  ___ __ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
| (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
 \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                        |_|                     --By YSF

\033[00m''')
		print('[NOTE] Type "\033[1;32;48mclear()\033[00m" Anywhere To Clear The Screen')
		print('[NOTE] Type "\033[1;32;48mexit()\033[00m" Anywhere To Exit The Program')

			
	def encrypting(self):
		counter = 0
		self.letters_symbols = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation+' '
		running = True

		while running:
			
			if counter != 0:
				text = input("\n[+] Enter text ---> ")
			else:
				text = input("[+] Enter text ---> ")
				counter+=1

			if text == '99':
				time.sleep(0.5)
				self.decision()

			elif text == 'clear()':
				if osname == 'nt':
					wincls()
				else:
					clear()
				self.banner()
				print("\n\n[ :) ] Encrypting process Starting \... ( Press \033[1;32;48m99\033[00m to go back To main Menu )\n")
				self.encrypting()

			elif text == 'exit()':
				print("\n\n[-] Exiting Program \... Have a Nice day :)")
				time.sleep(0.5)
				sys.exit()


			encrypt_list = []

			for i in text:
				shifting = 0
				finding = self.letters_symbols.find(i)
				shifting = finding+3

				if shifting == 83:
					encrypt_list.append(shifting)
					continue

				elif shifting > 95:
					defer = len(self.letters_symbols)-finding
					defer = 0+defer+1
					encrypt_list.append(defer)

				else:
					encrypt_list.append(shifting)



			encrypt_list_text = []

			for i in encrypt_list:
				encrypt_list_text.append(self.letters_symbols[i])


			encrypted = ''.join(encrypt_list_text)

			print('\n\n\033[1;32;48mEncrypted Text --->\033[00m',encrypted,'\n')



	def decrypting(self):
		counter = 0
		self.letters_symbols = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation+' '
		running = True

		while running:
			
			if counter != 0:
				text = input("\n[+] Enter text ---> ")
			else:
				text = input("[+] Enter text ---> ")
				counter+=1

			if text == '99':
				time.sleep(0.5)
				self.decision()

			elif text == 'clear()':
				if osname == 'nt':
					wincls()
				else:
					clear()
				self.banner()
				print("\n\n[ :) ] Decrypting process Starting \... ( Press \033[1;32;48m99\033[00m to go back To main Menu )\n")
				self.decrypting()

			elif text == 'exit()':
				print("\n\n[-] Exiting Program \... Have a Nice day :)")
				time.sleep(0.5)
				sys.exit()

			decrypt_list = []

			for i in text:
				shifting = 0
				finding = self.letters_symbols.find(i)
				shifting = finding-3

				if shifting == 83:
					decrypt_list.append(shifting)
					continue

				elif shifting < 0:
					get = self.letters_symbols[shifting]
					get1 = self.letters_symbols.find(get)
					decrypt_list.append(get1)
					continue

				else:
					decrypt_list.append(shifting)




			decrypt_list_text = []

			for i in decrypt_list:
				decrypt_list_text.append(self.letters_symbols[i])


			decrypted = ''.join(decrypt_list_text)

			print('\n\n\033[1;32;48mDecrypted Text --->\033[00m',decrypted,'\n')


		self.decrypting()




	def decision(self):
		dec = input("\n\nDo You Want To Encrypt [\033[1;32;48mE\033[00m] / Decrypt [\033[1;32;48mD\033[00m] / Exit ---> ")
		if dec == 'E':
			print("\n\n[ :) ] Encrypting process Starting \... ( Press \033[1;32;48m99\033[00m to go back To main Menu )\n")
			time.sleep(1) #1
			self.encrypting()

		elif dec == "clear()":
			if osname == 'nt':
				wincls()
			else:
				clear()
			self.banner()
			self.decision()

		elif dec == 'Exit' or dec == 'exit' or dec == 'exit()':
			command = input("[*] Do you want to Really Exit the program (Y/n) ---> ")

			if command == 'Y' or command == 'Yes' or command == 'y' or command == 'yes' or command == '' or command == ' ':
				print("\n\n[-] Exiting Program \... Have a Nice day :)")
				time.sleep(0.5)
				sys.exit()

		elif dec == 'D':
			print("\n\n[ :) ] Decrypting process Starting \... ( Press \033[1;32;48m99\033[00m to go back To main Menu )\n")
			time.sleep(1)
			self.decrypting()

		else:
			print("\n[*] Command not recognized. Let's try that again ...\n")
			self.decision()


main = Main()
