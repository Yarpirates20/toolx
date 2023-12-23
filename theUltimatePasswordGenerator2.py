from pyfiglet import Figlet
from termcolor import colored
import requests
from bs4 import BeautifulSoup
from string import punctuation
import time
from joblib import Parallel, delayed

words = []

def displayHeader():
    figlet = Figlet(font="small")
    header = figlet.renderText("The UPG")
    print(colored(header,"blue"))

def displayMenu():
    print(colored("=" * 24 + " Password Generation Options" + "=" * 24, "cyan"))
    print()
    print(colored("\t 1 ", "magenta"), colored(" - Scrape Webpage for List", "yellow"))
    print(colored("\t 2 ", "magenta"), colored(" - Munge Textfile", "yellow"))
    print(colored("\t 99 ", "magenta"), colored("- Quit Program", "yellow"))
    print()
    
def leet(word, lvl):
	words = []
	for i in range(1,lvl):
		if i == 1:
			words.append( word.replace('e', '3') )
			words.append( word.replace('a', '4') )
			words.append( word.replace('s', '5') )
			words.append( word.replace('o', '0') )
			words.append( word.replace('i', '!') )
			words.append( word.replace('l', '!') )
			words.append( word.replace('a', '@') )
		if i == 2:
			temp = word
			temp = temp.replace('a', '@')
			temp = temp.replace('i', '1')
			words.append( temp )
			
		if i == 3:
			temp = temp.replace('s', '$')
			temp = temp.replace('a', '@')
			temp = temp.replace('i', '1')
			words.append( temp )
		if i == 4:
			# leet speak combo one from munge.py
			temp = word
			temp = temp.replace('e', '3')
			temp = temp.replace('a', '4')
			temp = temp.replace('o', '0')
			temp = temp.replace('i', '1')
			temp = temp.replace('s', '$')
			words.append( temp )
		if i == 5:
			# leet speak combo two from munge.py
			temp = word
			temp = temp.replace('e', '3')
			temp = temp.replace('a', '@')
			temp = temp.replace('o', '0')
			temp = temp.replace('i', '1')
			temp = temp.replace('s', '$')
			words.append( temp )
		if i == 6:
			# leet speak combo three from munge.py
			temp = word
			temp = temp.replace('e', '3')
			temp = temp.replace('a', '4')
			temp = temp.replace('o', '0')
			temp = temp.replace('i', '!')
			temp = temp.replace('s', '$')
			words.append( temp )
		if i == 7:
			# leet speak combo five from munge.py
			temp = word
			temp = temp.replace('e', '3')
			temp = temp.replace('a', '4')
			temp = temp.replace('o', '0')
			temp = temp.replace('l', '1')
			temp = temp.replace('s', '$')
			words.append( temp )		
		
	return set(words)

def appendCharacter(word):
	words = []
	for i in range(33,65):
		words.append(word + chr(i))
		
	for i in range(91,96):
		words.append(word + chr(i))
		
	for i in range(123,127):
		words.append(word + chr(i))
		
	return words

def mungeWord(word):
	words = []
	words.append(leet(word, 8))
	return words
	
def capitalize(word, index):
	char = word[index].upper()
	new = word[:index] + char + word[index+1:]
	return new
	
def createBaseList(lines):
	words = []
	for line in lines:
		line = line.strip()
		words.append(line)
			
		endCap = capitalize(line.lower(), len(line) - 1)
		startCap = capitalize(line.lower(), 0)
		words.append(endCap)
		words.append(startCap)
						
		words.append(line.upper())
		words.append(line.lower())
	return words


def main():
	displayHeader()
	displayMenu()
	selection = 0

	while selection != 99:
		selection = input("Enter selection: ")
		if selection.isdigit():
			selection = int(selection)
			if selection == 1:
				url = input("Enter url to page to scrape: ")
				page = requests.get(url)
				if page.ok:
					soup = BeautifulSoup(page.content, "html.parser")
					select = input("Enter selection criteria: ")
					outfile = input("Enter outfile name: ")
					links = soup.select(select)
					f = open(outfile, 'a')
					for link in links:
						word = link.text.replace('"', '').replace(" ", '')
						words = link.text.replace('"','').strip()
						word = word.strip()
						f.write(f"{word}\n")
						f.write(f"{words}\n")

				else:
					print("ERROR: could not retrieve page!")

			elif selection == 2:
				words = []
				inputfile = input("Ener input file name: ")
				f = open(inputfile, "r")
				lines = f.readlines()
				f.close()
				outfile = input("Enter outfile name: ")
				numberOfRounds = int(input("Enter the number of rounds of munging: "))
				f = open(outfile, 'w')
				start = time.time()
				
				words = createBaseList(lines)
				
				for word in words:
					f.write(f"{word}\n")
						
				print(colored(f"Base list created with {len(words)} unique passwords!", "green"))
				count = len(words)
				step = 0
				
				print(colored("Starting to munge list!", "cyan"))
				wordSets = Parallel(n_jobs=2)(
					delayed(mungeWord)(word) for word in words
				)
				
				for wordSet in wordSets:
					for word in wordSet[0]:
						words.append(word)
						
				
				for i in range(1, numberOfRounds+1):
					temp = words
					wordSets = Parallel(n_jobs=2)(
						delayed(appendCharacter)(word)for word in temp
					)
		
					for wordSet in wordSets:
						for word in wordSet:
							temp.append(word)
					words = temp
					
					for word in words:
						f.write(f"{word}\n")
					count = count + len(words)
					print(colored(f"Round {i} complete with a total of {count} unique passwords!", "green"))
					timeCheck = time.time()
					if timeCheck % 300 == 0 and timeCheck > step:
						print(colored(f"Time Elapsed: {time.time()-start}", "cyan"))
						step = int(time.time() - start) 
				
						
							
					
				f.close()

			else:
				print(colored("Invalid Selection!", "red"))

main()
