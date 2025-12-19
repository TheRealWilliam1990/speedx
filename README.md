# SpeedX - Dynamic Gear Visualization System

A Python application that provides a dynamic graphical visualization of a gear system with automatic shift mechanism.

## Features

- **Dynamic Gear Visualization**: Real-time animation of two rotating gears
- **Auto-Shift Mechanism**: Automatically adjusts gear levels based on gear ratio
- **Physics Integration**: Uses the GearSystem class for accurate speed calculations
- **Interactive Display**: Shows current gear level, input speed, gear ratio, and output speed

## Requirements

- Python 3.x
- matplotlib
- numpy

## Installation

Install the required dependencies:

```bash
pip install matplotlib numpy
```

## Usage

Run the application:

```bash
python main.py
```

This will open a matplotlib window showing:
- A blue circle (input gear) on the left
- A red circle (output gear) on the right
- Rotation markers showing the gears spinning
- Current gear level (e.g., "3/5") at the top
- Speed and ratio information at the bottom

The gears will animate continuously, with the gear level automatically adjusting based on the gear ratio every 60 frames.

## How It Works

1. **Input Gear (Blue)**: Rotates at a constant speed in one direction
2. **Output Gear (Red)**: Rotates in the opposite direction at a speed determined by the gear ratio
3. **Gear Ratio**: Changes periodically between [1.3, 0.9, 0.7, 1.5]
4. **Auto-Shift**: Adjusts the current gear level based on the ratio:
   - Shifts up if ratio > 1.2 and not at max gear
   - Shifts down if ratio < 0.8 and not at min gear
   - Maintains current gear otherwise

## Code Structure

- `main.py`: Entry point with visualization and animation logic
- `gear_physics.py`: GearSystem class for physics calculations
- `GearVisualizer`: Class handling the matplotlib visualization
- `auto_shift()`: Function for automatic gear shifting logic

## Animation Details

- Frame rate: 20 FPS (50ms interval)
- Rotation speed: 6 degrees per frame for input gear
- Output gear speed: Calculated based on gear ratio (opposite direction)
- Gear size bounds: 0.5 to 2.0 radius units (for visibility)

## License

Author: TheRealWilliam1990
Date: 2025-12-19
