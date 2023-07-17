"""
Author: masakokh
Year: 2022
Version: 1.0.0
Note:
Package: base class
"""
# built-in
# internal


class ErrorBase:
	"""

	"""

	def __init__(self, defaultValue: bool= False):
		"""

		"""
		self.__code	= 0
		self.__found	= defaultValue
		self.__message	= ''

	def getCode(self) -> int:
		"""

		:return:
		"""
		return self.__code

	def getMessage(self) -> str:
		"""

		:return:
		"""
		return self.__message

	def isYes(self) -> bool:
		"""

		:return:
		"""
		return self.__found

	def setNo(self) -> None:
		"""

		:return:
		"""
		self.__code	= 0
		self.__found	= False
		self.__message	= ''

	def setYes(self, code: int= 0, message: str= '') -> None:
		"""

		:param code:
		:param message:
		:return:
		"""
		self.__code	= code
		self.__found	= True
		self.__message	= message
