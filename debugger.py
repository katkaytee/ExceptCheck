# Author: Katherine Tan 2018

import string


# Dump the tokens and tree for a given Java file.
def displayTokensAndTree(tokens, tree):
	print tokens
	for path, node in tree:
		print path, node
	print "------------"
	