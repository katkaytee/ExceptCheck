# Author: Katherine Tan 2018

import sys


# Simple script to strip out newlines in a given file and replace with spaces.
def replaceNewlines():
	clean = open(sys.argv[2]).read().replace('\n', ' ')
	print clean


# Format a list of copy-pasted Exceptions to be in Python syntax.
def formatExceptions():
	clean = open(sys.argv[2]).read().replace(', ', '\" : \"Exception\", \\\n\"')
	print clean


def main():
	if sys.argv[1] == '-n':
		replaceNewlines()
	elif sys.argv[1] == '-e':
		formatExceptions()
	
if __name__ == "__main__":
	main()
