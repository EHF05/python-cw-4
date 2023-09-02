def my_name():
   
    print("My name is essa")
my_name() 

def my_meal(food,drink):
    
    print(f"i like to eat {food} and while drinking {drink}")
my_meal("kfc","cola")


def cube(number): 
    
    return number**3
print(cube(9))
    
def by_three(number):
    if number % 3==0:

        result=cube(number)
        print(f"the answer is {result}")
        return result
    
    else:
      return print("False")
by_three(8)







    


