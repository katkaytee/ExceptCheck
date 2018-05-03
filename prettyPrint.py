# Author: Katherine Tan 2018

import string
import sys

from exceptData import *


class PrettyColors:
	"""Colors for pretty printing"""
	ENDC = '\033[0m'
	OKBLUE = '\033[94m'
	WARNING = '\033[93m'


def abortWarning(beginPosition):
	print PrettyColors.WARNING + \
		"\t\tpotential early abort in catch at line " + \
		str(beginPosition[0]) + PrettyColors.ENDC


def emptyWarning(beginPosition):
	print PrettyColors.WARNING + "\t\tempty catch at line " + \
		str(beginPosition[0]) + PrettyColors.ENDC


def loggingOnlyWarning(beginPosition):
	print PrettyColors.WARNING + \
		"\t\tpotential logging only in catch at line " + \
		str(beginPosition[0]) + PrettyColors.ENDC


def noCatches(tryPosition):
	print PrettyColors.WARNING + \
		"\t\tno catch blocks found for try statement at line " + \
		str(tryPosition[0]) + PrettyColors.ENDC


def throwableWarning(beginPosition):
	print PrettyColors.WARNING + \
		"\t\tThrowable overcatch at line " + \
		str(beginPosition[0]) + PrettyColors.ENDC


def todoWarning(lineno):
	print PrettyColors.WARNING + "\t\tTODO or FIXME in catch at line " + \
		str(lineno) + PrettyColors.ENDC


def catchOrderWarning(tryPosition):
	print PrettyColors.WARNING + \
		"\t\tunreachable catch blocks for try statement at line " + \
		str(tryPosition[0]) + PrettyColors.ENDC


def printCatchBlockBounds(beginPosition, endPosition, start):
	if start:
		print PrettyColors.OKBLUE + "\t\tblock begins at line " + \
			str(beginPosition[0]) + " column " + str(beginPosition[1]) + \
			PrettyColors.ENDC
	else:
		print PrettyColors.OKBLUE + "\t\tblock ends at line " + \
			str(endPosition[0]) + " column " + str(endPosition[1]) + \
			PrettyColors.ENDC


def printExceptions(exceptionList):
	for e in exceptionList:
		print PrettyColors.OKBLUE + "\t>> catch block for " + e + \
			PrettyColors.ENDC


def printSummary(exceptData):
	print "\n----------EXCEPTION SUMMARY----------"
	print "Warnings found in the following files:"
	for filename in exceptData.warningFiles:
		print filename
	print "-------------------------------------"
	print "Todo warnings in files:"
	for filename in exceptData.todoFiles:
		print filename
	print "-------------------------------------"
	print "Empty catch warnings in files:"
	for filename in exceptData.emptyFiles:
		print filename
	print "-------------------------------------"
	print "Logging only warnings in files:"
	for filename in exceptData.loggingOnlyFiles:
		print filename
	print "-------------------------------------"
	print "Abort warnings in files:"
	for filename in exceptData.abortFiles:
		print filename
	print "-------------------------------------"
	print "Throwable warnings in files:"
	for filename in exceptData.throwableFiles:
		print filename
	print "-------------------------------------"
	print "Unreachable catches in files:"
	for filename in exceptData.catchOrderFiles:
		print filename
	print "-------------------------------------"
	print str(exceptData.tryCount) + " try blocks found"
	print str(exceptData.catchCount) + " catch blocks found"
	print str(exceptData.warningCount) + " warnings/bad practices found in " + \
		str(len(exceptData.warningFiles)) + " files"	
	print str(exceptData.todoCount) + " todo warnings"
	print str(exceptData.emptyCount) + " empty catch warnings"
	print str(exceptData.loggingOnlyCount) + " logging only warnings"
	print str(exceptData.abortCount) + " abort warnings"
	print str(exceptData.throwableCount) + " caught Throwable warnings"
	print str(exceptData.catchOrderCount) + " unreachable catch warnings\n"


def printTryFound(beginPosition):
	print PrettyColors.OKBLUE + "  >> try statement found at line " + \
		str(beginPosition[0]) + " column " + str(beginPosition[1]) + \
		PrettyColors.ENDC
