
class car():
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        
    def set_brand(self,userBrand):
        self.__brand = userBrand
        
    def get_brand(self):
        return self.__brand;
        
    def full_Name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol Or Diesel"
    
class ElectricCar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Battery"
    

my_tesla = ElectricCar("Tesla","Model S","85kWh")
print(my_tesla.fuel_type())


safari = car("Tata", "Safari")
print(safari.fuel_type())
        
# my_car = car("Toyota","Corolla")
# print(my_car.full_Name())