# Author - Gaurav Chakraverty, Student ID - 22750993
# CITS1401 Computational Thinking with Python - Project2 submission
# Gaurav_22750993_Project2.py - A python program that can calculate the
# distribution of digits for numbers found in a certain file.


# main function that takes in the name of a csv file
def main(filename,no_places,regularise=False):
    # validate the file and inputs
    valid,errmsg = inputvalidator(filename,no_places,regularise)
    if (valid == False):
        print(errmsg)
        return[]
    # open the file and set as read
    openfile = open(filename, 'r')
    # store all lines in the file as a list
    readlines = openfile.readlines()
    openfile.close()
    # extract all the numbers as integers
    intonlylist = intextractor(readlines)
    # convert all the integers to positive
    posintlist = neg2pos(intonlylist)
    # two types of output possible
    outputlist,fracoutput=calculations(no_places,posintlist)
    if(regularise==False):
        return outputlist
    if(regularise==True):
        return fracoutput
    return []


# function to validate the file and the inputs
# checks if file is there and can be opened
# checks if inputs to the main function are of the expected type
def inputvalidator(filename,no_places,regularise=False):
    valid = True
    errmsg = ""
    # regularise can only be boolean or 0 or 1.
    if ((type(regularise) != bool) and (regularise!=0) and (regularise!=1)):
        valid = False
        errmsg = errmsg + "Invalid Input: regularise must be True/False. \n"
    # no_places can only be an integer.
    if ((type(no_places) != int)):
        valid = False
        errmsg = errmsg + "Invalid Input: no_places must be an Integer. \n"
    # no_places can only be greater than 0.
    if ((type(no_places) == int) and (no_places<=0)):
        valid = False
        errmsg = errmsg + "Invalid Input: no_places must be greater than 0. \n"
    # filename can only be a string.
    if (type(filename) != str):
        valid = False
        errmsg = errmsg + "Invalid Input: filename must be a string. \n"
    # check if file exists and can be opened.
    if (type(filename) == str):
        try:
            x = open(filename, 'r')
            x.close()
        except FileNotFoundError:
            valid = False
            errmsg = errmsg + "Invalid Input: Given filename cannot be found. \n"
        except IOError:
            valid = False
            errmsg = errmsg +"Error: Unable to open the specied file."
    return valid,errmsg
        
        
# function to extract the integer values       
def intextractor(readlines):
    intonlylist = []
    for row in range(0, len(readlines)):
        currentrow = readlines[row].split(',')
        for rowitem in range(0,len(currentrow)):
            try:
                intonlylist.append(int(float(currentrow[rowitem])))
            except:
                pass
    return intonlylist
        
        
# function to convert all the integers to positive        
def neg2pos(intonlylist):
    posintlist = []
    for number in range(0,len(intonlylist)):
        posnumber = int(((intonlylist[number])**2)**(0.5))
        posintlist.append(posnumber)
    return posintlist


# function to convert each numcount to a fraction of numcounts
def num2frac(numcounter):
    tempcounts = numcounter
    sumcount = 0
    fraclist = []
    for count1 in range(0,len(tempcounts)):
        sumcount = sumcount + tempcounts[count1]
    for count2 in range(0,len(tempcounts)):
        frac = round(float(tempcounts[count2]/sumcount), 4)
        fraclist.append(frac)
    return fraclist


# function that goes through each digit of the extracted integers one by one
# and keeps counting how many times each digit is a specific number.
def calculations(no_places,posintlist):
    # keeps count how many times each number appears for the current position
    numcounter = [0,0,0,0,0,0,0,0,0,0]
    outputlist = []
    fracoutput = []
    # executes the whole loop for each number position
    # if number is smaller than the number position we are looking at
    # then it just skips that number
    for places in range(0,no_places):
        for number in range(0,len(posintlist)):
            currentnumber = posintlist[number]
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='0'):
                numcounter[9]=numcounter[9]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='1'):
                numcounter[0]=numcounter[0]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='2'):
                numcounter[1]=numcounter[1]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='3'):
                numcounter[2]=numcounter[2]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='4'):
                numcounter[3]=numcounter[3]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='5'):
                numcounter[4]=numcounter[4]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='6'):
                numcounter[5]=numcounter[5]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='7'):
                numcounter[6]=numcounter[6]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='8'):
                numcounter[7]=numcounter[7]+1
            if((len(str(currentnumber))>=places+1) and (str(currentnumber)[places])=='9'):
                numcounter[8]=numcounter[8]+1
        # after each loop keep appending the numcounter to the outputlist
        outputlist.append(numcounter)
        # we need to also keep making a fraclist
        fraclist = num2frac(numcounter)
        # then after calculating our fraclist we append it to our fracoutput
        fracoutput.append(fraclist)
        # must reset numcounter for the next loop to use it
        numcounter = [0,0,0,0,0,0,0,0,0,0]
    # normal output and fraction version of the output
    return outputlist,fracoutput
    