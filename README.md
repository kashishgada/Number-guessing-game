Python Number Guessing Game
A simple, interactive command-line game built with Python. This project was created to practice loops, conditional logic, and error handling.


🚀 How it Works
The program generates a random integer between 1 and 100.

The user is prompted to guess the number in the terminal.

The program provides feedback:

"Number is too low" if the guess is under the target.

"Number is too high" if the guess is over the target.

If the user enters something that isn't a number (like text), the program handles the error gracefully using a try-except block.

The game ends when the user guesses the correct number.


🛠️ Features
Randomization: Uses Python's built-in random library.

Input Validation: Prevents the program from crashing if the user types a non-integer.

Infinite Loop: Uses while True to allow multiple attempts until the win condition is met.


📋 Requirements
Python 3.x


🖥️ How to Run
Clone this repository or download the script.

Open your terminal or command prompt.

Run the following command:

python game.py



🧠 What I Learned
How to import and use Python libraries.

Implementing Type Casting (converting input strings to integers).

Using Exception Handling (ValueError) to improve the user experience.
