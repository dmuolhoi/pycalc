# About CLI Calculator

## Version 1.0.0

CLI Calculator is a powerful command-line tool that provides basic arithmetic operations with an elegant and user-friendly interface.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Multiple Number Input**: Perform operations on multiple numbers at once
- **Rich Text Interface**: Colorful and well-formatted command-line interface
- **Comprehensive Error Handling**: Clear error messages for all potential issues
- **Modular Design**: Well-organized code structure for maintainability
- **Global Commands**: Access help and exit functions from anywhere

## Technical Details

This calculator is built with Python and uses the following technologies:

- **Rich Library**: For beautiful terminal formatting and colors
- **JSON Configuration**: For error and message management
- **Modular Architecture**: Separate modules for different operations
- **Markdown Documentation**: Comprehensive help and about information

## Usage

Run the calculator by executing `python main.py` from the command line.

## Development

The calculator is organized into several modules:

  - set_1/
    - commands/
      - errors.json
      - messages.json
    - data/
      - about.md
      - help.md
    - operations/
      - _init_.py
      - addition.py
      - subtraction.py
      - multiplication.py
      - division.py
    - main.py
    - README.md