#----------------------------------------------------------------------|

class Vehicle():
    """Vehicle parent class"""
    def __init__(self, make, model, kpl):
        self.make = make
        self.model = model
        self.fuel = 0
        self.max_fuel = 0
        self.kpl = kpl


    def refuel(self, litres):
        """refuels vehicle by [input] Litres upto max_fuel"""
        self.fuel += litres
        if self.fuel > self.max_fuel:
        
            print(
                "Woah there buddy, your tank is overflowing!" 
                f"{litres - self.max_fuel} Litres of fuel flow on the ground!"
                )
            self.fuel = self.max_fuel
        self.fuel_level()


    def fuel_level(self):
        """Outputs to terminal Vehicle fuel level"""
        print(f"You've got {self.fuel} Litres left in the tank")

    def travel(self, distance):
        """Simulate vehicle travel - consumes fuel"""
        fuel_used = distance / self.kpl

        if fuel_used > self.fuel:
            print(
                "*chug* *chug* chug* you ran out of gas! \n"
                f"You only travelled {self.fuel * self.kpl:.0f}km, "
                "I guess your walking the next "
                f"{distance -self.fuel * self.kpl:.0f} km"
                )
            return self.fuel * self.kpl
        else:
            print("Brrooom! Made it there in record time!")
            return distance

class Car(Vehicle):
    """Car class - child of vehicle class"""
    def __init__(self, make, model, kpl):
        super().__init__(make, model, kpl)
        self.max_fuel = 50
        self.windows_up = True


    def wind_up_windows(self):
        if self.windows_up:
            print("The windows are already up!, quit messing around!")
        else:
            self.windows_up = True
            print("Windows are up, that'll keep the rabble is out!")

class Motorbike(Vehicle):
    """Motorbike class - child of vehcile class"""
    def __init__(self, make, model, kpl):
        super().__init__(make, model, kpl)
        self.max_fuel = 15
        self.kpl = 25

    def wheelie(self):
        print("You pull a sick wheelie!")

#Tesst runs

civic = Vehicle("Honda", "Civic", 15)
civic2 = Car("Honda", "Civic", 15)
low_rider = Motorbike("Harley Davidson", "Low Rider", 25)

low_rider.refuel(55)
low_rider.refuel(2)
civic2.refuel(55)
civic2.refuel(5)


print(civic)
print(civic.__dict__)
print(civic2)
print(civic2.__dict__)
print(low_rider)
print(low_rider.__dict__)
civic2.fuel_level()

low_rider.travel(10)
low_rider.travel(1000)