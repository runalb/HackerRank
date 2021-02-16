"""
Task
Given an integer, , perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of  to , print Not Weird
If N is even and in the inclusive range of  to , print Weird
If N is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
"""


N = int(input())
if (N % 2 == 1) :
    print("Weird")

else:
    if(N >= 2 and N<=5) :
        print("Not Weird")

    elif (N >= 6 and N<=20):
        print("Weird")

    elif (N>20):
        print("Not Weird")


