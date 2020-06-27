'''
Name: numbers.py
Author: Harinath Selvaraj
Date: 27 June 2020
Version: 1.00
Description: Python Program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”
'''
print ([ 'ThreeFive' if ((x % 3 ==0) & (x % 5 == 0)) else
  'Three' if (x % 3 == 0) else
  'Five' if (x % 5 == 0) else x  
for x in range(1, 101) ])