from equ import *
import re

print ("Welcome to Table Top Calculator")

operators = ("+","-","*","=","(",")")
reservedWords = ("to","add","help","quit","q", "print", "math","+","-","*","=","(",")")

atrList = dict()
exit = False

while exit == False:
    text = input(">> ")
    command = text.split(" ")
    print(text)

    if command[0] in ("quit","q"):
        exit = True
        break

    elif command[0] == "add":
        if len(command) <= 1: #TODO make sure attributes contain no math
            print("add needs at least one argument")
        else:
            for atr in command[1:]:
                if atr in reservedWords:
                    print("Can't add " + atr + " because it is reserved")
                    continue

                atrList[atr]= [0,0] #value, visited

    elif command[0] == "set":
        if len(command) <= 1:
            print("set needs at least 2 arguments")
        else:
            changeList=[]
            toFound = False
            for i in range(1,len(command)):
                if command[i] == "to":
                    toFound = True
                    break
                else:
                    changeList.append(command[i])

            if len(changeList) == 0:
                print("No attributes given")
            elif toFound == False:
                print("Missing \"to\"")
            elif len(command) == i + 1:
                print("set \"to\" what?")
            elif command[i + 1].isalpha():#add grammar
                print("Can't set attribute to " + command[i+1])
            else:
                val = int(command[i+1])
                for atr in changeList:
                    #check if the atr actually exists
                    if atr in atrList:
                        atrList[atr][0] = val
                    else:
                        print("Cant find " + atr)


    elif command[0] == "print":
        #should add specificity
        maxLen = 0 #should add a global maxLen
        for atr in atrList.keys():
            if len(atr) > maxLen:
                maxLen = len(atr)

        for atr in iter(atrList):
            print(atr.ljust(maxLen, " ") + " = " + str(atrList[atr][0]))


    elif command[0] == "math":
        for eq in command[1:]:
            newEquation = re.split("(\s+|\+|\-|\*|\(|\))",eq)
            newEquation = [x for x in newEquation if x != '']
            print(newEquation)
            evalEqu(newEquation,atrList)

    elif command[0] == "help":
        print("good")
    else:
        print("Not a command")
