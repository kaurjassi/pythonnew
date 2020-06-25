def decorator_function(any_function):
	def wrapper_function(*args, **kwargs):
		"""This is wrapper function"""
		print("this is awesome fnction")
		return any_function(*args , **kwargs)
	return wrapper_function
	
@decorator_function
def add(a,b,c):
	"""This function take numbers as input and return the addition of these three numbers. """
	return a+b+c


print(add(6,7,8))
print(add.__doc__)
	


