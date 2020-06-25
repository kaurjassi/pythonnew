def divide(a,b):
      try:
            return a/b
      except ZeroDivisionError:
            return "you cannot divide with zero"    # here we also print  desired msg....
      except TypeError as err:
            return "you enter string instead of integer"     # here we also print  desired msg....
      except:
            return "unexpected error"    

print(divide(10,0))

       

            
      

               