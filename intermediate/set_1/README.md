# CLI INTERMEDIATE SET_2

A comprehensive command-line calculator built with Python, featuring basic arithmetic operations and an elegant user interface.

## Features

- Addition, subtraction, multiplication, and division operations
- Support for multiple number inputs
- Rich text interface with colors and formatting
- Comprehensive error handling
- Global help and exit commands
- Clear screen functionality
- Modular code organization
- JSON-based error and message management

## Project Structure

```
calculator/
├── operations/
│   ├── __init__.py
│   ├── addition.py
│   ├── subtraction.py
│   ├── multiplication.py
│   └── division.py
├── commands/
│   ├── errors.json
│   └── messages.json
├── data/
│   ├── help.md
│   └── about.md
├── main.py
└── README.md
```

## Requirements

- Python 3.6 or higher
- Rich library for terminal formatting

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:

```bash
pip install rich
```

## Usage

Run the calculator with:

```bash
python main.py
```

### Global Commands

- `help` - Display help information
- `exit`, `quit`, `q`, `x` - Exit the calculator

## License

This project is open source and available for personal and commercial use.

## Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request.