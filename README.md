# Python GUI Calculator

A simple and elegant graphical calculator built with Python's tkinter library.

![Calculator](https://img.shields.io/badge/Python-3.6+-blue.svg)
![GUI](https://img.shields.io/badge/GUI-tkinter-green.svg)

## Features

- Clean and intuitive graphical user interface
- Basic arithmetic operations: addition (+), subtraction (−), multiplication (×), division (÷)
- Additional functions: percentage (%), sign toggle (±), clear (C)
- Decimal number support
- Error handling for invalid operations
- Keyboard-like button layout similar to standard calculators

## Requirements

- Python 3.6 or higher
- tkinter (included with most Python installations)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd python-gui-calculator
   ```

2. No additional dependencies need to be installed as tkinter comes with Python by default.

## Usage

### Running the Calculator

```bash
python calculator.py
```

Or make it executable and run directly:

```bash
chmod +x calculator.py
./calculator.py
```

### Using the Calculator

- **Number Input**: Click number buttons (0-9) to enter numbers
- **Decimal**: Click the "." button to add decimal points
- **Basic Operations**: 
  - `+` for addition
  - `−` for subtraction  
  - `×` for multiplication
  - `÷` for division
- **Special Functions**:
  - `C` clears the current calculation
  - `±` toggles the sign of the current number
  - `%` converts the current number to a percentage
- **Calculate**: Press `=` to perform the calculation

### Example Operations

- Basic calculation: `5 + 3 = 8`
- Decimal calculation: `10.5 × 2 = 21`
- Percentage: `50 % = 0.5`
- Sign toggle: `5 ± = -5`

## Project Structure

```
python-gui-calculator/
├── calculator.py          # Main application file
├── requirements.txt       # Python dependencies (empty - uses built-ins)
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## Code Overview

The calculator is implemented using object-oriented programming:

- **Calculator class**: Main application class that handles the GUI and logic
- **Event-driven programming**: Button clicks trigger corresponding methods
- **State management**: Tracks current number, previous number, and pending operations
- **Error handling**: Gracefully handles division by zero and invalid inputs

## Development

### Running Tests

Currently, no automated tests are included. Manual testing can be performed by:

1. Testing all basic operations
2. Testing edge cases (division by zero, multiple decimal points)
3. Testing the special functions (clear, percentage, sign toggle)

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

Potential improvements for future versions:

- Keyboard input support
- Scientific calculator functions (sin, cos, tan, log, etc.)
- Memory functions (M+, M-, MR, MC)
- History of calculations
- Themes and customizable appearance
- Unit tests