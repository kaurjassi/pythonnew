#def convert_string(l):
 #   string_list = []
  #  for i in l:
      #  if type(i) == int:
   #        string_list.append(str(i))
    #return string_list



def convert_string2(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float)]

numbers = [1,2.0,3, [4,5,6] ,'true','false']
print(convert_string2(numbers))        

    