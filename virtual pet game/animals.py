cat =  '''
 C A T                

 /\_/\ \n           
( o.o ) \n          
 > ^ < \n           


'''                   

dog = '''
 D O G                                                             
  __      _ 
o'')}____// 
 `_/      ) 
 (_(_/-(_/  

'''

bird = '''
 B I R D
 ,_
>' )
( ( \ 
''|

'''

dog_1 = "Dog"
cat_2 = "Cat"
bird_3 = "Bird"


while True:
    questions = input("Choose your favorite animal ? %s - , %s - , %s : " % (dog_1, cat_2, bird_3))
    if questions == "Dog":
        print("\n Congratulations!! You have chosen a :\n")
        print(dog)
    elif questions == "Cat":
        print("\n Congratulations!! You have chosen a :\n")
        print(cat)
    elif questions == "Bird":
        print("\n Congratulations!! You have chosen a :\n")
        print(bird)
    else:
        print("Please Chose your favorite animal")
    

