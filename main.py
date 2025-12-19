"""
main.py

This is the entry point for the speedx application. The implemented functionality includes:
- Auto-shift mechanism for optimized performance

Author: TheRealWilliam1990
Date: 2025-12-19
"""

def auto_shift(gear_ratio, current_gear, max_gear):
    """
    Automatically shifts the gear to optimize performance.

    Args:
        gear_ratio (float): The current gear ratio
        current_gear (int): The current gear of the application
        max_gear (int): The maximum allowable gear

    Returns:
        int: The new gear after auto-shifting
    """
    if gear_ratio > 1.2 and current_gear < max_gear:
        print("Shifting up a gear...")
        return current_gear + 1
    elif gear_ratio < 0.8 and current_gear > 1:
        print("Shifting down a gear...")
        return current_gear - 1
    else:
        print("Maintaining current gear...")
        return current_gear


def main():
    """
    The main function that initializes and runs the speedx application.
    """
    print("Welcome to SpeedX Auto-Shift System!")

    # Example application parameters
    current_gear = 3
    max_gear = 5

    # Simulated input data (gear ratios from sensors or calculations)
    gear_ratios = [1.3, 0.9, 0.7, 1.5]

    # Process each gear ratio and adjust current gear
    for ratio in gear_ratios:
        print(f"Current Gear: {current_gear}, Gear Ratio: {ratio}")
        current_gear = auto_shift(ratio, current_gear, max_gear)
        print(f"New Gear: {current_gear}\n")

    print("SpeedX system exiting. Goodbye!")


if __name__ == "__main__":
    main()