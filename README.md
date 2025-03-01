# Password Strength Checker

## Project Overview
The Password Strength Checker is a Python-based program that evaluates the security level of a given password. It uses predefined criteria to determine whether a password is weak, moderate, or strong. The program provides immediate feedback, helping users improve their password security.

## Features
- **Length Requirement** – Ensures the password meets a minimum length.
- **Character Variety** – Checks for a mix of uppercase and lowercase letters.
- **Numerical Requirement** – Ensures the password includes at least one number.
- **Special Characters** – Encourages the use of symbols for added security.
- **Feedback System** – Provides real-time feedback based on the strength of the password.

## How It Works
1. The user inputs a password.
2. The program evaluates the password against security criteria.
3. A strength score is assigned based on the number of requirements met.
4. The program displays feedback indicating whether the password is **weak, moderate, or strong**.
5. If the password is weak, the program provides **suggestions for improvement**.

## Technology Used
- **Python** – The core programming language used for logic and evaluation.
- **Regular Expressions (`re` module)** – Used to detect specific patterns in the password, such as uppercase letters, numbers, and special characters.
- **Command Line Interface (CLI)** – A simple interface where users enter their passwords and receive feedback instantly.

## Installation and Usage

### **Prerequisites**
- Python must be installed on the system.
- Or you can use your designated compiler 

### **Steps to Run the Program**
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script:
   ```sh
   cd path/to/your/project
