# Author: Katherine Tan 2018

import os
import javalang

from collections import defaultdict


# Take a list of tokens and return a list of lists organized by line number.
def getTokenDict(tokens):
	tokenDict = defaultdict(list)
	for token in tokens:
		tokenDict[token.position[0]].append(token)
	return tokenDict


# Return True if the methodName indicates some kind of logging.
def isLogging(methodName):
	if methodName.lower().find("print") != -1 or \
		methodName.lower().find("log") != -1 or \
		methodName.lower().find("error") != -1:
		return True
	else:
		return False


# Return a list of embedded methods. The way the AST is set up, there may be
# another MethodInvocation in the top-level selectors or arguments parameter.
def findEmbeddedMethods(expression, embeddedList):
	for arg in expression.arguments:
		if isinstance(arg, javalang.tree.MethodInvocation):
			argMethodName = arg.member
			embeddedList.append(argMethodName)
			findEmbeddedMethods(arg, embeddedList)
	if expression.selectors:
		for selector in expression.selectors:
			if isinstance(selector, javalang.tree.MethodInvocation):
				selectorMethodName = selector.member
				embeddedList.append(selectorMethodName)
				findEmbeddedMethods(selector, embeddedList)
	return embeddedList


# Look for a token within the specified range that is a return, break, or 
# continue token. Return the line number at which the token was found, else -1.
def searchExitToken(tokenDict, start, end):
	for i in range(start, end + 1):
		for token in tokenDict[i]:
			if token.value == "continue" or token.value == "break" or \
				token.value == "return":
				return token.position[0]
	return -1


# Look for StatementExpressions that are of type Assignment. Returns a list of
# javalang.tree.MemberReference objects.
def findAssignedVars(tryBlock):
	assignedVars = []
	for statement in tryBlock:
		if isinstance(statement, javalang.tree.StatementExpression) and \
			isinstance(statement.expression, javalang.tree.Assignment):
			memberReference = statement.expression.expressionl
			if hasattr(memberReference, "member"):
				assignedVars.append(memberReference)
	return assignedVars


# Return a list of caught Exceptions.
def findCaughtExceptions(catches):
	exceptionList = []
	for catchClause in catches:
		exceptionList.extend(catchClause.parameter.types)
	return exceptionList


# Return True if an IfStatement immediately follows the TryStatement
# in the AST. This means that the IfStatement is the right sibling 
# of TryStatement.
def ifStatementFollows(path):
	siblings = path[-1]
	for i, statement in enumerate(siblings):
		if isinstance(statement, javalang.tree.TryStatement):
			if len(siblings) - 1 > i and \
				isinstance(siblings[i + 1], javalang.tree.IfStatement):
				return siblings[i + 1]
	return False


# Check if variable shows up in any of the method or embedded methods' 
# arguments.
def varFoundInArgs(expression, variable):
	for arg in expression.arguments:
		if isinstance(arg, javalang.tree.MemberReference) and \
			variable.member == arg.member:
			return True
		elif isinstance(arg, javalang.tree.MethodInvocation):
			if varFoundInArgs(arg, variable):
				return True

	if expression.selectors:
		for selector in expression.selectors:
			if isinstance(selector, javalang.tree.MethodInvocation):
				if varFoundInArgs(selector, variable):
					return True
	return False


# Check if any of the variables assigned in the try statement beforehand
# are now being checked in this if statement.
def ifContainsVar(varsToCheck, ifStatement):
	condition = ifStatement.condition
	if isinstance(condition, javalang.tree.MemberReference):
		for var in varsToCheck:
			if var.member == condition.member:
				return True
	elif isinstance(condition, javalang.tree.BinaryOperation):
		for var in varsToCheck:
			if isinstance(condition.operandl, javalang.tree.MemberReference) and \
				var.member == condition.operandl.member:
				return True
			elif isinstance(condition.operandr, javalang.tree.MemberReference) and \
				var.member == condition.operandr.member:
				return True
	elif isinstance(condition, javalang.tree.MethodInvocation):
		for var in varsToCheck:
			if varFoundInArgs(condition, var):
				return True
	return False
