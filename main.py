"""
main.py

This is the entry point for the speedx application. The implemented functionality includes:
- Auto-shift mechanism for optimized performance
- Dynamic graphical visualization of gears using matplotlib

Author: TheRealWilliam1990
Date: 2025-12-19
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import numpy as np
from gear_physics import GearSystem


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
        return current_gear + 1
    elif gear_ratio < 0.8 and current_gear > 1:
        return current_gear - 1
    else:
        return current_gear


class GearVisualizer:
    """
    A class to handle the visualization of rotating gears.
    """
    
    def __init__(self):
        """Initialize the gear visualizer with figure and axes."""
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-3, 3)
        self.ax.set_aspect('equal')
        self.ax.set_title('SpeedX Dynamic Gear Visualization', fontsize=16, fontweight='bold')
        
        # Initialize gear parameters
        self.current_gear = 3
        self.max_gear = 5
        self.gear_ratios = [1.3, 0.9, 0.7, 1.5]
        self.current_ratio_index = 0
        self.input_speed = 100  # RPM
        
        # Create gear system
        self.gear_system = GearSystem(self.input_speed, self.gear_ratios[0])
        
        # Gear 1 (input gear) - left side
        self.gear1_radius = 1.0
        self.gear1_center = (-2, 0)
        self.gear1 = Circle(self.gear1_center, self.gear1_radius, 
                           fill=False, edgecolor='blue', linewidth=3)
        self.ax.add_patch(self.gear1)
        
        # Gear 2 (output gear) - right side, size based on gear ratio
        self.gear2_center = (2, 0)
        self.update_gear2_radius()
        self.gear2 = Circle(self.gear2_center, self.gear2_radius, 
                           fill=False, edgecolor='red', linewidth=3)
        self.ax.add_patch(self.gear2)
        
        # Gear markers (lines to show rotation)
        self.gear1_line, = self.ax.plot([], [], 'b-', linewidth=2)
        self.gear2_line, = self.ax.plot([], [], 'r-', linewidth=2)
        
        # Text display for gear info
        self.gear_text = self.ax.text(0, 2.5, '', fontsize=14, 
                                     ha='center', fontweight='bold')
        self.speed_text = self.ax.text(0, -2.5, '', fontsize=12, ha='center')
        
        # Animation variables
        self.angle1 = 0
        self.angle2 = 0
        self.frame_count = 0
        
    def update_gear2_radius(self):
        """Update gear 2 radius based on current gear ratio."""
        # Gear ratio determines the relative size with bounds to keep gears visible
        self.gear2_radius = max(0.5, min(2.0, self.gear1_radius * self.gear_system.gear_ratio))
        
    def animate(self, frame):
        """
        Animation function called for each frame.
        
        Args:
            frame: Frame number
        """
        # Update gear ratio periodically (every 60 frames)
        if frame % 60 == 0 and frame > 0:
            self.current_ratio_index = (self.current_ratio_index + 1) % len(self.gear_ratios)
            ratio = self.gear_ratios[self.current_ratio_index]
            
            # Update gear based on ratio
            self.current_gear = auto_shift(ratio, self.current_gear, self.max_gear)
            
            # Update gear system
            self.gear_system.gear_ratio = ratio
            
            # Update gear 2 visual
            self.update_gear2_radius()
            self.gear2.set_radius(self.gear2_radius)
        
        # Calculate rotation speeds (degrees per frame)
        # Input gear rotates based on input speed
        rotation_speed1 = 6  # degrees per frame
        
        # Output gear rotates in opposite direction, speed based on gear ratio
        rotation_speed2 = -rotation_speed1 / self.gear_system.gear_ratio
        
        # Update angles
        self.angle1 += rotation_speed1
        self.angle2 += rotation_speed2
        
        # Keep angles in range [0, 360)
        self.angle1 = self.angle1 % 360
        self.angle2 = self.angle2 % 360
        
        # Update gear markers (lines from center to edge)
        rad1 = np.radians(self.angle1)
        x1_start, y1_start = self.gear1_center
        x1_end = x1_start + self.gear1_radius * np.cos(rad1)
        y1_end = y1_start + self.gear1_radius * np.sin(rad1)
        self.gear1_line.set_data([x1_start, x1_end], [y1_start, y1_end])
        
        rad2 = np.radians(self.angle2)
        x2_start, y2_start = self.gear2_center
        x2_end = x2_start + self.gear2_radius * np.cos(rad2)
        y2_end = y2_start + self.gear2_radius * np.sin(rad2)
        self.gear2_line.set_data([x2_start, x2_end], [y2_start, y2_end])
        
        # Update text displays
        output_speed = self.gear_system.calculate_output_speed()
        self.gear_text.set_text(f'Current Gear: {self.current_gear}/{self.max_gear}')
        self.speed_text.set_text(
            f'Input Speed: {self.input_speed:.0f} RPM | '
            f'Gear Ratio: {self.gear_system.gear_ratio:.1f} | '
            f'Output Speed: {output_speed:.0f} RPM'
        )
        
        return self.gear1, self.gear2, self.gear1_line, self.gear2_line, self.gear_text, self.speed_text


def main():
    """
    The main function that initializes and runs the speedx application with visualization.
    """
    print("Welcome to SpeedX Auto-Shift System with Dynamic Gear Visualization!")
    
    # Create visualizer
    visualizer = GearVisualizer()
    
    # Create animation and store reference to prevent garbage collection
    visualizer.anim = animation.FuncAnimation(
        visualizer.fig, 
        visualizer.animate,
        frames=None,  # Infinite loop
        interval=50,  # 50ms between frames (20 FPS)
        blit=True
    )
    
    # Show the plot (blocks until window is closed)
    plt.show()
    
    print("SpeedX system exiting. Goodbye!")


if __name__ == "__main__":
    main()