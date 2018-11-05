# #1: Define a Vehicle class with the following attributes and methods:
# - `vehicle_type` 'str'
# - `wheel_count` 'int'
# - `name` 'str'
# - `cost` 'int'
# - `colors` 'str'
# - `vehicle_brand` 'str'
# - `mpg` 'dict', with the following properties:
#     - `city` 'int'
#     - `highway` 'int'
#     - `combined` 'int'
# - `get_vehicle_type` should return the `vehicle_type`
# - `get_vehicle_brand` should return the classes `vehicle_brand`
# - `get_vehicle_drive` if the `wheel_drive` for that class is "no wheels!" then
#     it should return "no wheels send it back to the shop" otherwise it should
#     return "I have "  + self.wheel_drive  + " wheel drive"
#
# Your Vehicle class should take one argument (a `dict`) with the above
# attributes. The methods should be defined on the class.


class vehicle:
    def __init__(self, vehicle, name, cost, colors, mpg):
        self.vehicle_type = str
        self.vehicle_count = int
        self.name = str
        self.cost = int
        self.colors = str
        self.vehicle_brand = str
        self.mpg = {
            mpg.city: int,
            mpg.highway: int,
            mpg.combined: int,
        }


# #2: Create a Motorcycle class that inherits from the Vehicle class and has the
# following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `pop_wheelie` 'bool', if `wheel_count` is not equal to 2 then it should be
#   False


# #3: Define a Car class with the following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `can_drive` that should return 'Vrrooooom Vroooom'


# #4: Define a Truck class with the following attributes and methods:
# - `wheel_drive` 'str', defaults to "no wheels!"
# - `rev_engine` that should return 'revvvvvreeeev'
class Truck:
    def __init__(self, wheel_count="no wheels!")


# Commit when you finish working on these questions!
