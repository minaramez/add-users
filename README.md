# Linux User Automation Script

This Python script is designed to automate the process of adding users to a Linux machine. It reads user data from a CSV file and performs various system operations to create user accounts.

## Prerequisites
- Python 3
- Linux operating system

## Usage
1. Ensure that the CSV file `linux_users.csv` is present in the same directory as the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script using the following command:
   ```
   python3 script.py
   ```
4. The script will read the user data from the CSV file and add the users to the Linux machine.
5. User accounts will be created with default passwords, which can be changed by the users on their first login.

## Script Details
The script performs the following operations:

1. Importing Required Libraries:
   - `csv`: Used to read and write CSV files.
   - `os`: Used for system-related operations.
   - `re`: Provides support for regular expressions.
   - `subprocess`: Used to run shell commands.

2. Clearing the Terminal:
   - The `subprocess.call('clear')` command clears the terminal screen.

3. Printing Script Information:
   - The script author's name, along with information about the script, is displayed.

4. User Data Format:
   - The expected format for user data in the CSV file is "Username:Password | Password Type".

5. Default Password:
   - The variable `default_password` is set to a default value ("password").

6. Checking Group Existence:
   - The function `check_group(group_name)` checks if a group exists and adds it if it doesn't.

7. Reading the CSV File:
   - The script reads the CSV file "linux_users.csv" located in the same directory.
   - The header row is skipped.

8. Adding Users:
   - For each row in the CSV file, the script checks if all required fields are present.
   - The script constructs a username by combining the first initial of the first name with the last name.
   - Duplicate usernames are handled by adding a number to the username.
   - The user's home directory is determined based on the department and username.
   - If the department directory does not exist, it is created.
   - The script checks if the specified group exists and creates it if it doesn't.
   - The default shell is set based on the group name.
   - Finally, the user is added using the `useradd` command as a subprocess.

9. Setting Passwords:
   - A default password is set for each user using the `chpasswd` command as a subprocess.
   - Users are prompted to change their passwords on their first login using the `passwd -e` command as a subprocess.

Note: If any errors occur during the user creation process, an error message is displayed.

## Note
This script is specifically designed to run on a Linux machine. Please ensure that you have the necessary permissions to add users and execute system commands.
