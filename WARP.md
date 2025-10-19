# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Commands

### Running the Application
```bash
python calculator.py
```

### Making the Script Executable
```bash
chmod +x calculator.py
./calculator.py
```

### Development Setup
No dependencies installation required - uses built-in Python libraries only:
- tkinter (GUI framework) 
- operator (mathematical operations)

Python 3.6+ is required for compatibility.

## Architecture

### Single-File Application Structure
This is a simple GUI calculator implemented as a single Python file with object-oriented design:

**Core Components:**
- `Calculator` class: Main application controller that manages both GUI and business logic
- Event-driven architecture: Button clicks trigger corresponding methods
- State management: Tracks `current`, `previous`, `operation`, and `new_number` state variables

**Key Methods:**
- `create_widgets()`: Sets up the tkinter GUI layout with display and button grid
- `button_click()`: Central dispatcher that routes button events to appropriate handlers
- `number_input()`: Handles numeric and decimal input with validation
- `set_operation()`: Manages arithmetic operations and chaining calculations
- `calculate()`: Executes pending operations using the operator module
- Special functions: `clear()`, `toggle_sign()`, `percentage()` for calculator features

**State Management Pattern:**
The calculator uses a simple state machine approach:
- `new_number`: Boolean flag indicating whether to start fresh input or append
- `previous`/`current`: String representations of operands
- `operation`: Current pending arithmetic operation
- Automatic calculation chaining when operations are selected consecutively

**GUI Layout:**
- Read-only Entry widget for display (row 0)
- 4x5 button grid with special handling for "0" button (spans 2 columns)
- Grid weight configuration for responsive layout

**Error Handling:**
- Division by zero detection and graceful error display
- Multiple decimal point prevention
- ValueError/ZeroDivisionError exception catching with error state reset

This architecture keeps all logic centralized in a single class while maintaining clear separation between GUI events, state management, and calculation logic.