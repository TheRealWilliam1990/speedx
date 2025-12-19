class GearSystem:
    """
    A class to represent a gear system in a mechanical setup. This class simulates gear interactions, 
    allowing for calculation of output speed, input-output ratio, and transmission effectiveness.
    """

    def __init__(self, input_speed, gear_ratio):
        """
        Initialize the gear system with an input speed (in rpm) and a gear ratio.

        :param input_speed: The input rotational speed in revolutions per minute (rpm).
        :param gear_ratio: The gear ratio (output teeth/input teeth).
        """
        self.input_speed = input_speed
        self.gear_ratio = gear_ratio

    def calculate_output_speed(self):
        """
        Calculate the output speed based on the input speed and gear ratio.

        :return: The output rotational speed in rpm.
        """
        return self.input_speed / self.gear_ratio

    def efficiency(self, loss_percentage):
        """
        Estimate the efficiency of the system by factoring in energy loss (as a percentage).

        :param loss_percentage: Energy loss percentage (e.g., 5 for 5% loss).
        :return: The effective output speed factoring in losses.
        """
        actual_output_speed = self.calculate_output_speed()
        return actual_output_speed * (1 - loss_percentage / 100)

# Example usage:
# gear_system = GearSystem(1500, 2)
# print(gear_system.calculate_output_speed())  # Output: 750 rpm
# print(gear_system.efficiency(10))  # Output: 675 rpm (accounting for 10% loss)