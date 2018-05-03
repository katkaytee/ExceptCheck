# Author: Katherine Tan 2018

import string


class JavaExceptions:
	"""
	Class for storing and looking up inheritance information for Java 
	Exceptions.
	"""

	def __init__(self):
		# Exceptions at 3 levels down the Java inheritance hierarchy taken from
		# official Java documentation at
		# https://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html.
		self.exceptionDict = { \
			"Exception" : "Throwable", \

			"AclNotFoundException" : "Exception", \
			"ActivationException" : "Exception", \
			"AlreadyBoundException" : "Exception", \
			"ApplicationException" : "Exception", \
			"AWTException" : "Exception", \
			"BackingStoreException" : "Exception", \
			"BadAttributeValueExpException" : "Exception", \
			"BadBinaryOpValueExpException" : "Exception", \
			"BadLocationException" : "Exception", \
			"BadStringOperationException" : "Exception", \
			"BrokenBarrierException" : "Exception", \
			"CertificateException" : "Exception", \
			"CloneNotSupportedException" : "Exception", \
			"DataFormatException" : "Exception", \
			"DatatypeConfigurationException" : "Exception", \
			"DestroyFailedException" : "Exception", \
			"ExecutionException" : "Exception", \
			"ExpandVetoException" : "Exception", \
			"FontFormatException" : "Exception", \
			"GeneralSecurityException" : "Exception", \
			"GSSException" : "Exception", \
			"IllegalClassFormatException" : "Exception", \
			"InterruptedException" : "Exception", \
			"IntrospectionException" : "Exception", \
			"InvalidApplicationException" : "Exception", \
			"InvalidMidiDataException" : "Exception", \
			"InvalidPreferencesFormatException" : "Exception", \
			"InvalidTargetObjectTypeException" : "Exception", \
			"IOException" : "Exception", \
			"JAXBException" : "Exception", \
			"JMException" : "Exception", \
			"KeySelectorException" : "Exception", \
			"LastOwnerException" : "Exception", \
			"LineUnavailableException" : "Exception", \
			"MarshalException" : "Exception", \
			"MidiUnavailableException" : "Exception", \
			"MimeTypeParseException" : "Exception", \
			"MimeTypeParseException" : "Exception", \
			"NamingException" : "Exception", \
			"NoninvertibleTransformException" : "Exception", \
			"NotBoundException" : "Exception", \
			"NotOwnerException" : "Exception", \
			"ParseException" : "Exception", \
			"ParserConfigurationException" : "Exception", \
			"PrinterException" : "Exception", \
			"PrintException" : "Exception", \
			"PrivilegedActionException" : "Exception", \
			"PropertyVetoException" : "Exception", \
			"ReflectiveOperationException" : "Exception", \
			"RefreshFailedException" : "Exception", \
			"RemarshalException" : "Exception", \
			"RuntimeException" : "Exception", \
			"SAXException" : "Exception", \
			"ScriptException" : "Exception", \
			"ServerNotActiveException" : "Exception", \
			"SOAPException" : "Exception", \
			"SQLException" : "Exception", \
			"TimeoutException" : "Exception", \
			"TooManyListenersException" : "Exception", \
			"TransformerException" : "Exception", \
			"TransformException" : "Exception", \
			"UnmodifiableClassException" : "Exception", \
			"UnsupportedAudioFileException" : "Exception", \
			"UnsupportedCallbackException" : "Exception", \
			"UnsupportedFlavorException" : "Exception", \
			"UnsupportedLookAndFeelException" : "Exception", \
			"URIReferenceException" : "Exception", \
			"URISyntaxException" : "Exception", \
			"UserException" : "Exception", \
			"XAException" : "Exception", \
			"XMLParseException" : "Exception", \
			"XMLSignatureException" : "Exception", \
			"XMLStreamException" : "Exception", \
			"XPathException" : "Exception", \

			"UnknownGroupException" : "ActivationException", \
			"UnknownObjectException" : "ActivationException", \

			"CertificateEncodingException" : "CertificateException", \
			"CertificateExpiredException" : "CertificateException", \
			"CertificateNotYetValidException" : "CertificateException", \
			"CertificateParsingException" : "CertificateException", \

			"ServerCloneException" : "CloneNotSupportedException", \

			"BadPaddingException" : "GeneralSecurityException", \
			"CertificateException" : "GeneralSecurityException", \
			"CertPathBuilderException" : "GeneralSecurityException", \
			"CertPathValidatorException" : "GeneralSecurityException", \
			"CertStoreException" : "GeneralSecurityException", \
			"CRLException" : "GeneralSecurityException", \
			"DigestException" : "GeneralSecurityException", \
			"ExemptionMechanismException" : "GeneralSecurityException", \
			"IllegalBlockSizeException" : "GeneralSecurityException", \
			"InvalidAlgorithmParameterException" : "GeneralSecurityException", \
			"InvalidKeySpecException" : "GeneralSecurityException", \
			"InvalidParameterSpecException" : "GeneralSecurityException", \
			"KeyException" : "GeneralSecurityException", \
			"KeyStoreException" : "GeneralSecurityException", \
			"LoginException" : "GeneralSecurityException", \
			"NoSuchAlgorithmException" : "GeneralSecurityException", \
			"NoSuchPaddingException" : "GeneralSecurityException", \
			"NoSuchProviderException" : "GeneralSecurityException", \
			"ShortBufferException" : "GeneralSecurityException", \
			"SignatureException" : "GeneralSecurityException", \
			"UnrecoverableEntryException" : "GeneralSecurityException", \

			"ChangedCharSetException" : "IOException", \
			"CharacterCodingException" : "IOException", \
			"CharConversionException" : "IOException", \
			"ClosedChannelException" : "IOException", \
			"EOFException" : "IOException", \
			"FileLockInterruptionException" : "IOException", \
			"FileNotFoundException" : "IOException", \
			"FilerException" : "IOException", \
			"FileSystemException" : "IOException", \
			"HttpRetryException" : "IOException", \
			"IIOException" : "IOException", \
			"InterruptedByTimeoutException" : "IOException", \
			"InterruptedIOException" : "IOException", \
			"InvalidPropertiesFormatException" : "IOException", \
			"JMXProviderException" : "IOException", \
			"JMXServerErrorException" : "IOException", \
			"MalformedURLException" : "IOException", \
			"ObjectStreamException" : "IOException", \
			"ProtocolException" : "IOException", \
			"RemoteException" : "IOException", \
			"SaslException" : "IOException", \
			"SocketException" : "IOException", \
			"SSLException" : "IOException", \
			"SyncFailedException" : "IOException", \
			"UnknownHostException" : "IOException", \
			"UnknownServiceException" : "IOException", \
			"UnsupportedDataTypeException" : "IOException", \
			"UnsupportedEncodingException" : "IOException", \
			"UserPrincipalNotFoundException" : "IOException", \
			"UTFDataFormatException" : "IOException", \
			"ZipException" : "IOException", \

			"MarshalException" : "JAXBException", \
			"PropertyException" : "JAXBException", \
			"UnmarshalException" : "JAXBException", \
			"ValidationException" : "JAXBException", \

			"MBeanException" : "JMException", \
			"OpenDataException" : "JMException", \
			"OperationsException" : "JMException", \
			"ReflectionException" : "JMException", \
			"RelationException" : "JMException", \

			"AttributeInUseException" : "NamingException", \
			"AttributeModificationException" : "NamingException", \
			"CannotProceedException" : "NamingException", \
			"CommunicationException" : "NamingException", \
			"ConfigurationException" : "NamingException", \
			"ContextNotEmptyException" : "NamingException", \
			"InsufficientResourcesException" : "NamingException", \
			"InterruptedNamingException" : "NamingException", \
			"InvalidAttributeIdentifierException" : "NamingException", \
			"InvalidAttributesException" : "NamingException", \
			"InvalidAttributeValueException" : "NamingException", \
			"InvalidNameException" : "NamingException", \
			"InvalidSearchControlsException" : "NamingException", \
			"InvalidSearchFilterException" : "NamingException", \
			"LimitExceededException" : "NamingException", \
			"LinkException" : "NamingException", \
			"NameAlreadyBoundException" : "NamingException", \
			"NameNotFoundException" : "NamingException", \
			"NamingSecurityException" : "NamingException", \
			"NoInitialContextException" : "NamingException", \
			"NoSuchAttributeException" : "NamingException", \
			"NotContextException" : "NamingException", \
			"OperationNotSupportedException" : "NamingException", \
			"PartialResultException" : "NamingException", \
			"ReferralException" : "NamingException", \
			"SchemaViolationException" : "NamingException", \
			"ServiceUnavailableException" : "NamingException", \

			"PrinterAbortException" : "PrinterException", \
			"PrinterIOException" : "PrinterException", \

			"ClassNotFoundException" : "ReflectiveOperationException", \
			"IllegalAccessException" : "ReflectiveOperationException", \
			"InstantiationException" : "ReflectiveOperationException", \
			"InvocationTargetException" : "ReflectiveOperationException", \
			"NoSuchFieldException" : "ReflectiveOperationException", \
			"NoSuchMethodException" : "ReflectiveOperationException", \

			"AnnotationTypeMismatchException" : "RuntimeException", \
			"ArithmeticException" : "RuntimeException", \
			"ArrayStoreException" : "RuntimeException", \
			"BufferOverflowException" : "RuntimeException", \
			"BufferUnderflowException" : "RuntimeException", \
			"CannotRedoException" : "RuntimeException", \
			"CannotUndoException" : "RuntimeException", \
			"ClassCastException" : "RuntimeException", \
			"CMMException" : "RuntimeException", \
			"ConcurrentModificationException" : "RuntimeException", \
			"DataBindingException" : "RuntimeException", \
			"DOMException" : "RuntimeException", \
			"EmptyStackException" : "RuntimeException", \
			"EnumConstantNotPresentException" : "RuntimeException", \
			"EventException" : "RuntimeException", \
			"FileSystemAlreadyExistsException" : "RuntimeException", \
			"FileSystemNotFoundException" : "RuntimeException", \
			"IllegalArgumentException" : "RuntimeException", \
			"IllegalMonitorStateException" : "RuntimeException", \
			"IllegalPathStateException" : "RuntimeException", \
			"IllegalStateException" : "RuntimeException", \
			"IllformedLocaleException" : "RuntimeException", \
			"ImagingOpException" : "RuntimeException", \
			"IncompleteAnnotationException" : "RuntimeException", \
			"IndexOutOfBoundsException" : "RuntimeException", \
			"JMRuntimeException" : "RuntimeException", \
			"LSException" : "RuntimeException", \
			"MalformedParameterizedTypeException" : "RuntimeException", \
			"MirroredTypesException" : "RuntimeException", \
			"MissingResourceException" : "RuntimeException", \
			"NegativeArraySizeException" : "RuntimeException", \
			"NoSuchElementException" : "RuntimeException", \
			"NoSuchMechanismException" : "RuntimeException", \
			"NullPointerException" : "RuntimeException", \
			"ProfileDataException" : "RuntimeException", \
			"ProviderException" : "RuntimeException", \
			"ProviderNotFoundException" : "RuntimeException", \
			"RasterFormatException" : "RuntimeException", \
			"RejectedExecutionException" : "RuntimeException", \
			"SecurityException" : "RuntimeException", \
			"SystemException" : "RuntimeException", \
			"TypeConstraintException" : "RuntimeException", \
			"TypeNotPresentException" : "RuntimeException", \
			"UndeclaredThrowableException" : "RuntimeException", \
			"UnknownEntityException" : "RuntimeException", \
			"UnmodifiableSetException" : "RuntimeException", \
			"UnsupportedOperationException" : "RuntimeException", \
			"WebServiceException" : "RuntimeException", \
			"WrongMethodTypeException" : "RuntimeException", \

			"SAXNotRecognizedException" : "SAXException", \
			"SAXNotSupportedException" : "SAXException", \
			"SAXParseException" : "SAXException", \

			"BatchUpdateException" : "SQLException", \
			"RowSetWarning" : "SQLException", \
			"SerialException" : "SQLException", \
			"SQLClientInfoException" : "SQLException", \
			"SQLNonTransientException" : "SQLException", \
			"SQLRecoverableException" : "SQLException", \
			"SQLTransientException" : "SQLException", \
			"SQLWarning" : "SQLException", \
			"SyncFactoryException" : "SQLException", \
			"SyncProviderException" : "SQLException", \

			"TransformerConfigurationException" : "TransformerException" \
		}


	# Check if child inherits from parent.
	def inherits(self, child, parent):
		if parent == child:
			return False
		elif parent == "Throwable":
			return True
		elif "Error" in child:
			return False
		elif child not in self.exceptionDict and parent == "Exception":
			return True
		# No way to know if child inherits from parent.
		elif child not in self.exceptionDict:
			return False
		else:
			c = child
			while c != "Throwable":
				if self.exceptionDict[c] == parent:
					return True
				else:
					c = self.exceptionDict[c]
			return False
