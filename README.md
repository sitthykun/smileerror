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
   		self.error.setFalse()

   		try:
	 		return inputData / 0
	
		exception Exception as e:
  			self.error.setTrue(message= str(e))
  			return -1


# render code
test	= TestClass()
result	= test.divideByZero(22)

if test.error.isTrue():
	print(f'Show the messag error please {test.error.getMessage()}')
```

