# Day 6: Let's Review

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for x in range(0,t):

    str = input()
    reseven = ""
    resodd = ""

    for x in range(0,len(str),2):
        #print(str[x])
        reseven = reseven + str[x]
    #print(reseven)

    for x in range(1, len(str), 2):
        # print(str[x])
        resodd = resodd + str[x]
    #print(resodd)

    print(reseven,resodd)

