import pytest

# Define custom exception class for a broken vehicle part
class BrokenVehiclePartError(Exception):
    print("Inside parent class BrokenVehiclePartError")
    pass

# Define a base class for vehicles
class Vehicle:
    print("Inside parent class Vehicle")

    def __init__(self, make, model):
        # Initialize vehicle with make and model
        self.make = make
        self.model = model

    def display_info(self):
        # Display information about the vehicle
        return f"{self.make} {self.model}"

# Define a child class for cars, inheriting from the Vehicle class
class Car(Vehicle):
    print("Inside child class Car")
    pass

# Define a child class for trucks, inheriting from the Vehicle class
class Truck(Vehicle):
    print("Inside child class Truck")
    pass

# Define a custom exception class for a flat tire, inheriting from BrokenVehiclePartError
class FlatTireError(BrokenVehiclePartError):
    print("Inside child class FlatTireError")
    pass

# Define a custom exception class for a busted hitch, inheriting from BrokenVehiclePartError
class BustedHitchError(BrokenVehiclePartError):
    print("Inside child class BrokenVehiclePartError")
    pass

# Function to simulate a vehicle issue
def simulate_vehicle_issue(vehicle):
    # Set the probability of encountering an issue
    issue_probability = 0.3  # Adjust probability as needed

    # Check for different issues based on probability
    if issue_probability > 0.5:
        # Raise a FlatTireError if a flat tire is detected
        raise FlatTireError(f"Flat tire detected on {vehicle.display_info()}!")
    elif issue_probability > 0.2:
        # Raise a BustedHitchError if a busted hitch is detected
        raise BustedHitchError(f"Busted hitch detected on {vehicle.display_info()}!")
    elif issue_probability < 0:
        # Raise a generic exception for a crash program error (currently commented out)
        raise  # crashProgramError()
    else:
        # Print a message if no issues are detected
        print(f"No issues detected on {vehicle.display_info()}.")

# Entry point for the script
if __name__ == "__main__":
    # Create instances of Car and Truck
    car1 = Car("Toyota", "Camry")
    truck1 = Truck("Ford", "F-150")

    try:
        # Attempt to simulate issues with both vehicles
        simulate_vehicle_issue(car1)
        simulate_vehicle_issue(truck1)
    except BrokenVehiclePartError as e:
        # Handle BrokenVehiclePartError and print the caught exception
        print("----------try block executed----------")
        print(f"Caught exception: {e}")

    # Print vehicle information after the simulation
    print("\nVehicle Information:")
    print("Car 1:", car1.display_info())
    print("Truck 1:", truck1.display_info())

# PyTest tests
def test_vehicle_instantiation():
    # Test vehicle instantiation and display information
    car = Car("Toyota", "Camry")
    truck = Truck("Ford", "F-150")
    assert car.display_info() == "Toyota Camry"
    assert truck.display_info() == "Ford F-150"

def test_flat_tire_exception():
    # Test FlatTireError exception handling for a car
    car = Car("Toyota", "Camry")
    with pytest.raises(FlatTireError, match="Flat tire detected on Toyota Camry!"):
        simulate_vehicle_issue(car)

def test_busted_hitch_exception():
    # Test BustedHitchError exception handling for a truck
    truck = Truck("Ford", "F-150")
    with pytest.raises(BustedHitchError, match="Busted hitch detected on Ford F-150!"):
        simulate_vehicle_issue(truck)

# Uncomment the next test to simulate an unhandled exception
# def test_unhandled_exception():
#     with pytest.raises(Exception, match="Unhandled exception!"):
#         raise Exception("Unhandled exception!")

