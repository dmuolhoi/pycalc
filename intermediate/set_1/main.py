#!/usr/bin/env python3
"""
Calculator CLI - Main entry point
A command-line calculator with basic arithmetic operations and more.
"""
import os
import sys
import json
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table
from rich.prompt import Prompt
from rich import box

# Import operation modules
from operations.addition import add_numbers
from operations.subtraction import subtract_numbers
from operations.multiplication import multiply_numbers
from operations.division import divide_numbers

# Initialize Rich console
console = Console()

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_json_file(file_path):
    """Load and return JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        console.print(f"[bold red]Error loading {file_path}: {str(e)}[/bold red]")
        return {}

# Load messages and errors
MESSAGES = load_json_file('commands/messages.json')
ERRORS = load_json_file('commands/errors.json')

def print_header():
    """Print the calculator header."""
    console.print(Panel.fit(
        "[bold cyan]CLI Calculator[/bold cyan]\n[italic]Type 'help' for assistance or 'exit' to quit[/italic]",
        border_style="green",
        padding=(1, 2)
    ))

def show_help():
    """Display help information."""
    try:
        with open('data/help.md', 'r') as help_file:
            help_content = help_file.read()
            clear_screen()
            console.print(Markdown(help_content))
            input("\nPress Enter to continue...")
    except Exception as e:
        console.print(f"[bold red]Error displaying help: {str(e)}[/bold red]")

def show_about():
    """Display about information."""
    try:
        with open('data/about.md', 'r') as about_file:
            about_content = about_file.read()
            clear_screen()
            console.print(Markdown(about_content))
            input("\nPress Enter to continue...")
    except Exception as e:
        console.print(f"[bold red]Error displaying about: {str(e)}[/bold red]")

def display_menu():
    """Display the main menu."""
    clear_screen()
    print_header()
    
    table = Table(box=box.ROUNDED, border_style="green")
    table.add_column("[bold green]Option[/bold green]", justify="center")
    table.add_column("[bold green]Description[/bold green]", justify="left")
    
    table.add_row("1", "Addition")
    table.add_row("2", "Subtraction")
    table.add_row("3", "Multiplication")
    table.add_row("4", "Division")
    table.add_row("5", "Help")
    table.add_row("6", "About")
    table.add_row("7", "Exit")
    
    console.print(table)

def get_numbers():
    """Get multiple numbers from user input."""
    numbers = []
    console.print("[bold]Enter numbers (one per line, type 'done' when finished):[/bold]")
    
    while True:
        num_input = Prompt.ask("[cyan]Number[/cyan]")
        
        if num_input.lower() in ['done', 'end', 'finish']:
            break
            
        if num_input.lower() in ['exit', 'quit', 'q', 'x']:
            sys.exit(0)
            
        if num_input.lower() == 'help':
            show_help()
            continue
            
        try:
            numbers.append(float(num_input))
        except ValueError:
            console.print(ERRORS.get("invalid_number", "Invalid number, please try again."), style="bold red")
    
    return numbers

def format_result(result):
    """Format the result to handle whole numbers nicely."""
    if result == int(result):
        return int(result)
    return result

def main():
    """Main function to run the calculator."""
    try:
        while True:
            display_menu()
            choice = Prompt.ask("[bold green]Select an option[/bold green]")
            
            # Check for global commands
            if choice.lower() in ['exit', 'quit', 'q', 'x', '7']:
                console.print(MESSAGES.get("goodbye", "Goodbye!"), style="bold cyan")
                break
                
            if choice.lower() in ['help', '5']:
                show_help()
                continue
                
            if choice.lower() in ['about', '6']:
                show_about()
                continue
                
            if choice == '1':  # Addition
                clear_screen()
                console.print("[bold green]Addition[/bold green]")
                numbers = get_numbers()
                
                if len(numbers) < 2:
                    console.print(ERRORS.get("insufficient_numbers", "At least two numbers are required."), style="bold red")
                else:
                    result = add_numbers(numbers)
                    console.print(f"[bold green]Result: {format_result(result)}[/bold green]")
                
            elif choice == '2':  # Subtraction
                clear_screen()
                console.print("[bold green]Subtraction[/bold green]")
                numbers = get_numbers()
                
                if len(numbers) < 2:
                    console.print(ERRORS.get("insufficient_numbers", "At least two numbers are required."), style="bold red")
                else:
                    result = subtract_numbers(numbers)
                    console.print(f"[bold green]Result: {format_result(result)}[/bold green]")
                
            elif choice == '3':  # Multiplication
                clear_screen()
                console.print("[bold green]Multiplication[/bold green]")
                numbers = get_numbers()
                
                if len(numbers) < 2:
                    console.print(ERRORS.get("insufficient_numbers", "At least two numbers are required."), style="bold red")
                else:
                    result = multiply_numbers(numbers)
                    console.print(f"[bold green]Result: {format_result(result)}[/bold green]")
                
            elif choice == '4':  # Division
                clear_screen()
                console.print("[bold green]Division[/bold green]")
                numbers = get_numbers()
                
                if len(numbers) < 2:
                    console.print(ERRORS.get("insufficient_numbers", "At least two numbers are required."), style="bold red")
                else:
                    try:
                        result = divide_numbers(numbers)
                        console.print(f"[bold green]Result: {format_result(result)}[/bold green]")
                    except ZeroDivisionError:
                        console.print(ERRORS.get("division_by_zero", "Error: Division by zero is not allowed."), style="bold red")
            else:
                console.print(ERRORS.get("invalid_option", "Invalid option. Please try again."), style="bold red")
            
            # Pause to see results
            input("\nPress Enter to continue...")
            
    except KeyboardInterrupt:
        console.print(MESSAGES.get("interrupted", "\nOperation interrupted. Goodbye!"), style="bold cyan")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {str(e)}[/bold red]")

if __name__ == "__main__":
    main()