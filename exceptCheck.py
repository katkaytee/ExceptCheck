# Author: Katherine Tan 2018

import argparse
import debugger
import javalang
import os
import prettyPrint
import string
import sys

from checkers import BytecodeChecker, SimpleChecker
from exceptData import *


class DirectoryHandler:
	"""Class for handling directory unpacking"""

	def __init__(self, dataTracker, dirname, args):
		self.dirname = dirname
		self.sourceCheck = args.sourceCheck
		self.dataTracker = dataTracker
		self.args = args


	# Recursively check all the files.
	def checkDir(self, dirname):
		# Root is the current path, subdirs are the directory files at the root,
		# and files are the non-directory files at the root
		for root, subdirs, files in os.walk(dirname):
			# Go through and check each file
			for filename in files:
				if not filename.endswith('.java'):
					continue
				elif self.sourceCheck:
					filePath = os.path.join(root, filename)
					if self.args.skip and filePath in self.args.skip:
						continue
					if self.args.debug:
						print filePath
					checker = \
						SimpleChecker(self.dataTracker, filePath, self.args)
					checker.check()
			# Go through the subdirectories and handle those
			for subdir in subdirs:
				dirPath = os.path.join(root, subdir)
				if self.args.debug:
					print dirPath
				self.checkDir(subdir)


def main():
	ec_parser = \
		argparse.ArgumentParser(description="ExceptCheck: Process java files.")
	# Option for field and directory names
	ec_parser.add_argument(
		'-f', \
		'--filename', \
		dest='filenames',\
		metavar='N', \
		nargs='+', \
		help="a list of java files to check")
	ec_parser.add_argument(
		'-d', \
	 	'--dirname', \
	 	dest='dirnames', \
	 	metavar='N', \
	 	nargs='+', \
		help="a list of java directories to check")
	# Option for running a check on the source code or the bytecode
	ec_parser.add_argument(
		'--sourceCheck', \
		dest='sourceCheck', \
		action='store_true', \
		help="check the source code of the specified files and directories")
	ec_parser.add_argument(
		'--bytecodeCheck', \
		dest='bytecodeCheck', \
		action='store_true', \
		help="check the bytecode of the specified files and directories")
	ec_parser.add_argument(
		'--summary', \
		dest='summary', \
		action='store_true', \
		help="print a summary of ExceptCheck findings")
	ec_parser.add_argument(
		'--skip', \
		dest='skip', \
		metavar='N', \
	 	nargs='+', \
		help="a list of java files to skip within a specified directory")
	ec_parser.add_argument(
		'-v', \
		'--verbose', \
		dest='verbose', \
		action='store_true', \
		help="print verbose output of ExceptCheck findings")
	ec_parser.add_argument(
		'-dbg', \
		'--debug', \
		dest='debug', \
		action='store_true', \
		help="print debug information for ExceptCheck findings")
	ec_parser.set_defaults(
		sourceCheck=False, \
		bytecodeCheck=False, \
		summary=False, \
		verbose=False,
		debug=False)

	args = ec_parser.parse_args()
	print(args)

	if args.filenames == None and args.dirnames == None:
		print("Error: Please specify a file or directory to check")
		return

	# By default, run a source code check if neither check type is specified
	if args.sourceCheck == False and args.bytecodeCheck == False:
		args.sourceCheck = True

	# Keep track of summary with ExceptData.
	# Summary should keep a count of all try and catch blocks found, as well
	# as total number of bad practices found.
	exceptData = ExceptData()

	if args.filenames:
		for filename in args.filenames:
			if args.sourceCheck:
				checker = SimpleChecker(exceptData, filename, args)
				checker.check()
			else:
				checker = BytecodeChecker(filename, option=False)
				checker.check()

	if args.dirnames:
		for dirname in args.dirnames:
			dirHandler = DirectoryHandler(exceptData, dirname, args)
			dirHandler.checkDir(dirname)

	if args.summary:
		prettyPrint.printSummary(exceptData)


if __name__ == "__main__":
	main()
