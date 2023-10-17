# Motor.py

class Motor:
    """A class to represent a car engine."""

    def __init__(self, cylinders, liters, aspiration, code):
        """Instantiation"""
        self.cylinders = cylinders
        self.liters = liters
        self.aspiration = str(aspiration)
        self.code = str(code)

    def get_horsepower(self):
        """Returns potential HP based on user input and available options."""
        if self.aspiration == "Turbocharged":
            return int(self.liters * 120)
        if self.aspiration == "Supercharged":
            return int(self.liters * 80 + self.liters * 80 / 2)
        if self.aspiration == "Naturally Aspirated":
            return int(self.liters * 80)

    def get_cost(self):
        """Returns cost to build the motor, based on user specifications."""
        if self.aspiration == "Turbocharged":
            return int(self.cylinders * self.liters * 100)
        elif self.aspiration == "Supercharged":
            return int(self.cylinders * self.liters * 150)
        else:
            return int(self.cylinders * self.liters * 50)

    def get_redline(self):
        """Returns the redline (max RPM) of the motor."""
        return int(self.cylinders / self.liters * 3000)

    def save_to_file(self, filename):
        """Save motor specifications to a text file."""
        with open(filename, 'w') as file:
            file.write(f"Cylinders: {self.cylinders}\n")
            file.write(f"Liters: {self.liters}\n")
            file.write(f"Aspiration: {self.aspiration}\n")
            file.write(f"Code: {self.code}\n")

    @classmethod
    def load_from_file(cls, filename):
        """Load motor specifications from a text file and create a Motor object."""
        with open(filename, 'r') as file:
            data = file.read().split('\n')
        cylinders = int(data[0].split(": ")[1])
        liters = float(data[1].split(": ")[1])
        aspiration = data[2].split(": ")[1]
        code = data[3].split(": ")[1]
        return cls(cylinders, liters, aspiration, code)

import unittest

class TestMotor(unittest.TestCase):
    def test_horsepower_calculation(self):
        motor = Motor(4, 2.0, "Turbocharged", "ABCD")
        self.assertEqual(motor.get_horsepower(), 240)

    def test_cost_calculation(self):
        motor = Motor(6, 3.0, "Supercharged", "EFGH")
        self.assertEqual(motor.get_cost(), 1350)

    def test_redline_calculation(self):
        motor = Motor(8, 5.0, "Naturally Aspirated", "IJKL")
        self.assertEqual(motor.get_redline(), 4800)

if __name__ == '__main__':
    unittest.main()
    