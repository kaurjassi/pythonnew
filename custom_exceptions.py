class NameTooShortError(ValueError):
      pass

def validate(name):
      if len(name) < 8 :
            raise NameTooShortError('Name Is Too Short')


username = input("Enter your name : ")
validate(username)
print(f"Hello {username}")      