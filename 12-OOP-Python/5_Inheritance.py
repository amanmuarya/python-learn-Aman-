class vehicle:
    company = "XYZ moter"

    def __init__(self, n_wheels, n_seat, milages):
        print( "this is brand naem")
        self.n_wheels = n_wheels
        self.n_seat = n_seat
        self.milages = milages

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels, {self.n_seat} seats, and a mileage of {self.milages}"


# v1 = vehicle(n_wheels=4, n_seat=3, milages=7)
# print(v1.get_details())

class car(vehicle):
    def  __init__ (self , car_type, car_drive): 
        print( "this is car name")
        self.car_type =car_type
        self.car_drive =car_drive

# Car class inheritance the vehicle class 
# car class is called child class/ derived vlass 
# vehicle class is called prarent class / base class 

c1 = car(n_wheels=4, n_seat=3, milages=7    )
print(c1.milages)
print(c1.n_wheels)
print(c1.get_details())