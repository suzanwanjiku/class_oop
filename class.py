# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# inherits from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  
        self.storage = storage
        self.battery = battery
    
    # Encapsulatinf private attributes
    __os = "Android"  
    
    def get_os(self):
        return self.__os
    
    def call(self, name):
        return f"Calling {name} from {self.brand} {self.model}..."
    
    def charge(self):
        return f"Charging {self.model}..."

# Creation of objects
phone1 = Smartphone("Samsung", "S23", "256GB", "4500mAh")
phone2 = Smartphone("Apple", "iPhone 14", "128GB", "3200mAh")

print(phone1.info())       
print(phone1.call("John"))
print("Operating System:", phone1.get_os())
print(phone2.charge())
