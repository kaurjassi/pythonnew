user = {}
name = input("what is your name :")
age = input("what is your age :")
fav_movies =input("your favourite movies seprated by comma :").split(",")
fav_songs = input("your favourite songs seprated with comma :").split(",")
user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
for key,value in user.items():
    print(f"{key} : {value}")
    
    