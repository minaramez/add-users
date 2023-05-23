#!/usr/bin/env python3

#above is the shebang line, which specifies the location of the python interpreter on the system.

#csv is used to read and write to csv files
import csv
#os is used to communicate with system related operations
import os
#re provides support for regular expressions
import re
#subprocess is used to run shell commands
import subprocess

# command to clear terminal
subprocess.call('clear' )

#print functions to show the student name and date, along with information about the script.
print(" ")
print(" ")
print("Script written by: Mina Ramez Farag")
print("")
print("       ***************************************")
print("       ****Linux - Users adding Automation****")
print("       ***************************************")
print("")
print("User data is typed as following:")
print("Username:password | password type")
print("")

#setting a default password to all users added.
default_password= "password"

#function to check if a group exists or not, and to add it if not. 
def check_group( group_name):
    try:
        subprocess.check_output(['getent', 'group', group_name] )
    except subprocess.CalledProcessError:
        subprocess.call([ 'groupadd', group_name])

#function to read the csv file in the given directory. 
with open('linux_users.csv','r') as file :
    csv_reader =csv.reader( file )
    #function to skip header row
    next(csv_reader )
    
    for row in csv_reader:
        #check if all required fields are present
        if all(row[:6] ):
            #function to get the username by adding the initial of the first name to the last name
            first_name= row[ 2].lower()
            #function to get the last name and to remove special characters if any. 
            last_name= re.sub( r'[^\w\s]','', row[1]).lower( ) 
            #function to add the intial of the first name to the last name 
            username = first_name[0 ] +last_name
            
            #function that checks for duplicate users and adds a number next to the second and so on 
            count=1
            while  True:
                try:
                    subprocess.check_output( ['getent', 'passwd', username])
                    count+= 1
                    username= first_name[0 ]+ last_name+ str(count)
                except subprocess.CalledProcessError:
                    break
            
            #function to find the directory if it already exists, or go to home
            department =row[5]
            home_dir =os.path.join('/home', department, username)
            
            #function that creates the directory inside the home directory if it doesnt already exist 
            if not os.path.exists( os.path.join('/home', department)):
                subprocess.call( ['mkdir', os.path.join('/home',department)])
            
            #function that checks if a group exists and makes it if it doesnt 
            group_name = row[6 ] if row[6] else 'unnamedgroup'
            check_group( group_name)
            
            #function to set default shell based on group
            default_shell= '/bin/csh' if group_name =='office' else '/bin/bash'
            
            #finally, function to add the user by running linux commands as subprocesses. 
            try:
                subprocess.call(['useradd', '-m', '-d' , home_dir, '-s', default_shell, '-g', group_name, username])
            except subprocess.CalledProcessError:
                print(" ")
                print(f"User account {username} was not added due to an error.")
            
            #function to set a default password for the user and prompt the user to change it on first log in
            subprocess.call(['echo',f"{username}:{default_password}", '|', 'chpasswd'] )
            subprocess.call(['passwd', '-e', username])
            print("")
        else:
            print(username, ": account was not added due to missing information.")
            print(" ")
