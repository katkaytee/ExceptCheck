# Author: Katherine Tan 2018

import javalang


class ExceptData:
	"""Object for holding ExceptCheck data to be reported to the user"""

	def __init__(self):
		self.tryCount = 0
		self.catchCount = 0
		self.warningCount = 0

		# Keep track of the filenames that generated warnings. This will be 
		# helpful for analyzing individual files and try-catch blocks.
		self.warningFiles = []
		self.todoFiles = []
		self.emptyFiles = []
		self.loggingOnlyFiles = []
		self.abortFiles = []
		# May modify this later to include cases of overcatch.
		self.throwableFiles = []
		self.catchOrderFiles = []

		self.todoCount = 0
		self.emptyCount = 0
		self.loggingOnlyCount = 0
		self.abortCount = 0
		self.throwableCount = 0
		self.catchOrderCount = 0


	def addwarningFile(self, filename):
		if filename not in self.warningFiles:
			self.warningFiles.append(filename)


	# Increment the warning counter and also add a warningFile.
	def updateNewWarning(self, newFilename):
		self.warningCount += 1
		self.addwarningFile(newFilename)


	def updateNewWarningForTodo(self, newFilename):
		self.updateNewWarning(newFilename)
		self.todoCount += 1
		if newFilename not in self.todoFiles:
			self.todoFiles.append(newFilename)


	def updateNewWarningForEmpty(self, newFilename):
		self.updateNewWarning(newFilename)
		self.emptyCount += 1
		if newFilename not in self.emptyFiles:
			self.emptyFiles.append(newFilename)


	def updateNewWarningForLoggingOnly(self, newFilename):
		self.updateNewWarning(newFilename)
		self.loggingOnlyCount += 1
		if newFilename not in self.loggingOnlyFiles:
			self.loggingOnlyFiles.append(newFilename)


	def updateNewWarningForAbort(self, newFilename):
		self.updateNewWarning(newFilename)
		self.abortCount += 1
		if newFilename not in self.abortFiles:
			self.abortFiles.append(newFilename)


	def updateNewWarningForThrowable(self, newFilename):
		self.updateNewWarning(newFilename)
		self.throwableCount += 1
		if newFilename not in self.throwableFiles:
			self.throwableFiles.append(newFilename)


	def updateNewWarningForCatchOrder(self, newFilename):
		self.updateNewWarning(newFilename)
		self.catchOrderCount += 1
		if newFilename not in self.catchOrderFiles:
			self.catchOrderFiles.append(newFilename)

