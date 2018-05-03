# Author: Katherine Tan 2018

import debugger
import itertools
import linecache
import javalang
import os
import prettyPrint
import re
import string
import sys

from exceptData import *
from javaExceptions import *
from helpers import *


class SimpleChecker:
	""" 
	Class for running Java source-code analysis on specified files or 
	directories.
	"""
	def __init__(self, dataTracker, filename, args):
		self.filename = filename
		self.tokens = None
		self.dataTracker = dataTracker
		self.verbose = args.verbose
		# Set the debug flag here.
		self.debug = args.debug
		self.javaExceptions = JavaExceptions()


	# Find instances of "TODO" or "FIXME" inside catch blocks
	def findAndReportTodo(self, catchClause):
		beginLine = catchClause.begin_position[0]
		endLine = catchClause.end_position[0]
		inComment = False

		for lineno in range(beginLine, endLine + 1):
			line = linecache.getline(self.filename, lineno)
			if self.debug:
				sys.stdout.write(line)
				sys.stdout.flush()

			commentIndex = line.find("//") 
			todoIndex = line.lower().find("todo")
			fixmeIndex = line.lower().find("fixme")
			multiStartIndex = line.find("/*")
			multiEndIndex = line.find("*/")

			# Cover the basic cases for multiline comments, ignore edge casing 
			# for now.
			if not inComment:
				# Switching to inComment
				if multiStartIndex != -1 and \
					(commentIndex == -1 or multiStartIndex < commentIndex):
					inComment = True
				# Single line comment
				elif commentIndex != -1 and \
					(todoIndex > commentIndex or fixmeIndex > commentIndex):
					self.dataTracker.updateNewWarningForTodo(self.filename)
					if self.verbose:
						prettyPrint.todoWarning(lineno)
			if inComment:
				# Found end of comment
				if multiEndIndex != -1:
					if (todoIndex != -1 and todoIndex < multiEndIndex) \
						or (fixmeIndex != -1 and fixmeIndex < multiEndIndex):
						self.dataTracker.updateNewWarningForTodo(self.filename)
						if self.verbose:
							prettyPrint.todoWarning(lineno)
					inComment = False
				# Continue in comment
				elif multiEndIndex == -1 and \
					(todoIndex != -1 or fixmeIndex != -1):
						self.dataTracker.updateNewWarningForTodo(self.filename)
						if self.verbose:
							prettyPrint.todoWarning(lineno)
					

	def findAndReportLoggingOnly(self, catchClause, ifContainsVarFlag):
		if catchClause.block == []:
			return
		if ifContainsVarFlag:
			return
		for param in catchClause.parameter.types:
			if param == "InterruptedException":
				return

		# Go through catchClause and figure out if there are only log or print
		# statements.
		# Each element in the list can either be a StatementExpression,
		# LocalVariableDeclaration, or ClassDeclaration.
		# print catchClause.__dict__
		for statement in catchClause.block:
			# print statement.__dict__
			# print statement.expression.__dict__
			# print statement.expression.selectors.__dict__
			# We're looking for a simple method call to "log" or "print"
			if isinstance(statement, javalang.tree.StatementExpression) and \
				isinstance(statement.expression, javalang.tree.MethodInvocation):
				methodName = statement.expression.member
				# print methodName
				# print statement.expression.arguments
				# for arg in statement.expression.arguments:
					# print arg.member
					# print arg.arguments
				if not isLogging(methodName):
					return
				else:
					embeddedMethods = \
						findEmbeddedMethods(statement.expression, list())
					loggingFound = False
					for method in embeddedMethods:
						if isLogging(methodName):
							loggingFound = True
							break
					if not loggingFound:
						return
			else:
				return
		self.dataTracker.updateNewWarningForLoggingOnly(self.filename)
		if self.verbose:
			prettyPrint.loggingOnlyWarning(catchClause.begin_position)


	def findAndReportAbort(self, catchClause):
		# Go thrugh catchClause and figure out if there are terminating methods,
		# consistent with what the Aspirator authors did.
		for statement in catchClause.block:
			if isinstance(statement, javalang.tree.StatementExpression) and \
				isinstance(statement.expression, javalang.tree.MethodInvocation):
				methodName = statement.expression.member
				if methodName.lower().find("terminat") != -1 or \
					methodName.lower().find("halt") != -1 or \
					methodName.lower().find("exit") != -1 or \
					methodName.lower().find("abort") != -1 or \
					methodName.lower().find("fatal") != -1:
					self.dataTracker.updateNewWarningForAbort(self.filename)
					if self.verbose:
						prettyPrint.abortWarning(catchClause.begin_position)


	# In Java, Throwable is the superclass of all Errors and Exceptions in the
	# language. Catching this is generally an overcatch.
	def findAndReportThrowable(self, catchClause):
		for param in catchClause.parameter.types:
			if param == "Throwable":
				self.dataTracker.updateNewWarningForThrowable(self.filename)
				if self.verbose:
					prettyPrint.throwableWarning(catchClause.begin_position)


	# Look for cases where the catch block is essentially empty.
	def findEmptyCatch(self, catchClause, ifContainsVarFlag):
		# Case: All the lines are print or log method calls.
		self.findAndReportLoggingOnly(catchClause, ifContainsVarFlag)
		# Case: Catch block contains a TODO.
		self.findAndReportTodo(catchClause)


	# Check that more specific exceptions come earlier than more 
	# general ones.
	def checkCatchOrder(self, exceptionList, tryPosition):
		for parent, child in itertools.combinations(exceptionList, 2):
			if self.javaExceptions.inherits(child, parent):
				self.dataTracker.updateNewWarningForCatchOrder(self.filename)
				if self.verbose:
					prettyPrint.catchOrderWarning(tryPosition)
				return


	# Run the checker.
	def check(self):
		if self.verbose:
			print "Checking source code for " + self.filename
		
		# Open file for reading and parsing
		f = open(self.filename, 'r')
		if f.mode == 'r':
			contents = f.read()

		# The tokenizer breaks up the contents into a list of valid Java tokens.
		# Tokens are JavaToken objects, and each carries position (line, column)
		# and value info.
		# The parser assembles an abstract syntax tree (AST) using the tokens.
		tokens = list(javalang.tokenizer.tokenize(contents))
		# Organize the tokens so that they're easier to use.
		tokenDict = getTokenDict(tokens)
		self.tokens = tokens
		tree = javalang.parser.parse(self.tokens)
		# if self.debug:
		# 	debugger.displayTokensAndTree(tokens, tree)

		# tree.filter returns a generator, so it can only be used once.
		# TryStatement contains: resources, block, catches, finally_block, 
		# and begin_position information.
		for path, tryNode in tree.filter(javalang.tree.TryStatement):
			# Found a new try block.
			self.dataTracker.tryCount += 1
			beginPosition = tryNode.begin_position
			if self.verbose:
				prettyPrint.printTryFound(beginPosition)

			# No catch blocks found.
			if not tryNode.catches:
				if self.verbose:
					prettyPrint.noCatches(beginPosition)
				continue

			# In the case that the try statement exits through a return, break, 
			# or continue token, it's fine if the catch block is empty.
			tryStartLine = beginPosition[0]
			tryEndLine = tryNode.catches[0].begin_position[0]
			exitTokenFound = \
				searchExitToken(tokenDict, tryStartLine, tryEndLine)

			# Get a list caught exceptions and check that the more specific
			# ones come first.
			caughtExceptions = findCaughtExceptions(tryNode.catches)
			self.checkCatchOrder(caughtExceptions, beginPosition)

			# Look for simple variable assignments within the tryNode.
			# If variables are assigned in the try statement and immediately
			# checked in an if statement afterwards, it is ok if the 
			# associated catch block is empty.
			varsToCheck = findAssignedVars(tryNode.block)
			ifStatement = ifStatementFollows(path)
			ifContainsVarFlag = False
			if ifStatement != False and ifContainsVar(varsToCheck, ifStatement):
				ifContainsVarFlag = True

			for catchClause in tryNode.catches:
				# Found a new catch block.
				self.dataTracker.catchCount += 1
				if self.verbose:
					prettyPrint.printExceptions(catchClause.parameter.types)
					prettyPrint.printCatchBlockBounds(
						catchClause.begin_position, \
						catchClause.end_position, \
						start=True)

				# Case: Catch block is empty, print warning.
				if (not (len(tryNode.catches) == 1 and exitTokenFound != -1)) and \
					not ifContainsVarFlag:
					if len(catchClause.block) == 0:
						self.dataTracker.updateNewWarning(self.filename)
						self.dataTracker.emptyCount += 1
						if self.verbose:
							prettyPrint.emptyWarning(catchClause.begin_position)

				# Case: Catch block is essentially empty.
				self.findEmptyCatch(catchClause, ifContainsVarFlag)
				# Case: Catch block calls abort or exit.
				self.findAndReportAbort(catchClause)
				# Case: Exception overcatch in catching a Throwable.
				self.findAndReportThrowable(catchClause)
			
				if self.verbose:
					prettyPrint.printCatchBlockBounds(
						catchClause.begin_position, \
						catchClause.end_position, \
						start=False)


class BytecodeChecker:
	"""Class for running bytecode analysis on specified files or directories"""

	def __init__ (self, filename, args):
		print()

	def check(self):
		print("Checking bytecode for " + filename + "...")
		# TODO: Use python-javatools to check the bytecode

