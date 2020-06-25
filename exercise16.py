def cube_finder(a):
    cube_numbers = {} 
    for i in range(1,a+1):
        cube_numbers[i] = i**3
    return cube_numbers    
        
        



print(cube_finder(10))
     
