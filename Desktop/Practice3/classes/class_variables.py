from dataclasses import dataclass

@dataclass
class Car:
    # Class variable
    wheels: int = 4 
    
    # Instance variables (shorthand)
    model: str
    color: str

my_car = Car(model="Tesla", color="Red")
print(my_car) 
# Output: Car(model='Tesla', color='Red', wheels=4)