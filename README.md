# smileerror
## version 1.0.1
To make it a standard structure

```
# external library
from smileerror.ErrorBase import ErrorBase
# or pypi
# from ErrorBase import ErrorBase


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
	
		except ZeroDivisionError as e:
			self.error.setTrue(code= 2, message= str(e))
			return -1
		
		except Exception as e:
  			self.error.setTrue(code= 1, message= str(e))
  			return -1


# render code
test	= TestClass()
result	= test.divideByZero(22)

if test.error.isTrue():
	print(f'Show the error message error: {test.error.getMessage()}')

# if there is a complex structure, let try by this way
if test.findCode(2):
	print(f'Show the error message error: {test.error.getMessage()}')
```

