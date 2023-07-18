# smile-pyerror
python error class is, to make it simple structure

```
# external library
from ErrorBase import ErrorBase
# or pypi
# from smilepyerror import ErrorBase


class TestClass:
	"""
 	"""
	def __init__(self):
 		"""
   		"""
	 	# private
	 	self.error	= ErrorBase()

   def divideByZero(self, inputData: int) -> float:
   		"""
	 	"""
   		self.error.setNo()

   		try:
	 		return inputData / 0
	
		exception Exception as e:
  			self.error.setYes(message= str(e))
  			return -1

   def isError(self) -> bool:
   		"""
	 	"""
   		return self.error.isError()

# render code
test	= TestClass()
result	= test.divideByZero(22)

if test.error.isError():
	print(f'Show the messag error please {test.error.getMessage()}')
```

