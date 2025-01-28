#
# Program Name: Salary Projections.py
#
# Author: Chelsie
#
# Copyright: Penn State University
#
# Date: 09/08/2024
#
# Description: This is a program that does salary projections over years with
#average increase.
# It will take the number of years, and a starting salary and
#project growth.
# All parameters can be updated in the program.
# Salary Projection Program Parameters


# Initialize variables used to track information from year to year
totsal = 0
increase = 0
#open a new file where all inputs will be read into
nf = open("newfile.txt","r")
#read in information
name=nf.readline() 
sal = float(nf.readline())
yearlyinc = float(nf.readline())
years = int(nf.readline())
age = int(nf.readline())
start_yr = int(nf.readline())

print(name)


#Fix the columns so that the columns have column headers
print("Year# Age#  Increase:$   Salary:$      Lifetime:$ ")
# Calculate Annual Salary, Lifetime Salary, and Annual Increase. Display Results.
for i in range (years):
    totsal = (totsal + sal)     
    print ('{:>2}'.format(i+start_yr),
        '{:>2}'.format(age+i),
        '{:>13,.2f}'.format(increase),
        '{:>13,.2f}'.format(sal),
        '{:>15,.2f}'.format(totsal))
    increase = sal * yearlyinc/100
    sal = sal + increase
# Wait for the user to close window when running just python script (outside of
#IDE)
input('Hit enter to terminate program:')
