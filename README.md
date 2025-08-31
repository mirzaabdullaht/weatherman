# Weatherman

This project is a command-line tool that analyzes weather data from text files using Python.

## Features

- Reads and parses weather data files
- Calculates highest, lowest, and average temperatures
- Displays results in a chart format in the terminal
- Supports monthly and yearly analysis via command-line flags

## Usage

1. Place your weather data `.txt` files in the `weather_data` folder.
2. Run the script from the terminal:

   ```
   python weatherman.py weather_data -c YYYY/MM -a YYYY/M -e YYYY
   ```

   Replace `YYYY` and `MM` with the desired year and month.

3. Example:
   ```
   python weatherman.py weather_data -c 2004/08 -a 2004/8 -e 2004
   ```

## Branching Workflow

- `main`: Main branch (do not work here for assignments).
- `dev`: Development branch.
- `weatherman-task`: Task/feature branch for assignment work.

## How to Submit

1. Push your changes to your task branch.
2. Create a Pull Request from your task branch into `dev`.
3. Submit the PR link in Google Classroom.

## Requirements

- Python 3.x
- PyCharm or any code editor

## Author

- [mirzaabdullaht](https://github.com/mirzaabdullaht)

