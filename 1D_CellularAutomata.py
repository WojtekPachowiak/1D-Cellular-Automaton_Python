import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import keyboard

#mpl.rcParams['toolbar'] = 'None'
#######################################################################################

def RuleNumberToArray(rule_number):
    # convert "rules" into an array of ones and zeros
    rule_number = min(rule_number,255) # prevent numbers greater than 255
    binary = bin(rule_number) #convert to binary
    array = np.array( list(binary[2:]), dtype="int") #turn binary into an array
    array = array[::-1] #reverse the array
    ruleArray = np.zeros(8, dtype = "int") #create the array of zeros
    ruleArray[0:len(array)] = array # merge both arrays
    return ruleArray


def ApplyRules(matrix,rules):
    #in this loop we try to match the triplets of zeros and ones
    #and if we match
    for i in range(matrix.shape[0]-1): ###rows
        for j in range(1,matrix.shape[1]-1):   ###columns

            # 0 0 0
            if  matrix[i][j-1] == 0 and matrix[i][j] == 0 and matrix[i][j+1] == 0:
                matrix[i+1][j] = rules[0]

            # 0 0 1
            elif  matrix[i][j-1] == 0 and matrix[i][j] == 0 and matrix[i][j+1] == 1:
                matrix[i+1][j] = rules[1]

            # 0 1 0
            elif  matrix[i][j-1] == 0 and matrix[i][j] == 1 and matrix[i][j+1] == 0:
                matrix[i+1][j] = rules[2]

            # 0 1 1
            elif  matrix[i][j-1] == 0 and matrix[i][j] == 1 and matrix[i][j+1] == 1:
                matrix[i+1][j] = rules[3]

            # 1 0 0
            elif  matrix[i][j-1] == 1 and matrix[i][j] == 0 and matrix[i][j+1] == 0:
                matrix[i+1][j] = rules[4]

            # 1 0 1
            elif  matrix[i][j-1] == 1 and matrix[i][j] == 0 and matrix[i][j+1] == 1:
                matrix[i+1][j] = rules[5]

            # 1 1 0
            elif  matrix[i][j-1] == 1 and matrix[i][j] == 1 and matrix[i][j+1] == 0:
                matrix[i+1][j] = rules[6]

            # 1 1 1
            elif  matrix[i][j-1] == 1 and matrix[i][j] == 1 and matrix[i][j+1] == 1:
                matrix[i+1][j] = rules[7]
    return matrix[:,1:-1]

#######################################################################################
#initialize a matrix
matrixSize = (100,100)
matrix = np.zeros(matrixSize,dtype="int")
matrix[:,[0,-1]] = 2
cellsOnLocations = [20,50,80]
matrix[0][cellsOnLocations] = 1

# Two ways of setting up the rules
rulesArray = np.array([1,0,0,0,1,1,1,1])
rulesNumber = 57    #57 is beautiful!
slideshow = False

#######################################################################################

if slideshow == False:
    #single plot
    plt.figure(figsize=(6, 7))
    rules = RuleNumberToArray(rulesNumber)
    cellularPattern = ApplyRules(matrix,rules)
    plt.axes([0.025, 0.025, 0.95, 0.95])
    plt.xticks([])
    plt.yticks([])
    plt.title("Rule {}".format(rulesNumber))
    plt.imshow(cellularPattern)
    plt.show()

else:
    #plot slideshow
    plt.figure(figsize=(6, 7))
    for i in range(255):
        rules = RuleNumberToArray(i)
        cellularPattern = ApplyRules(matrix,rules)
        plt.clf()
        plt.axes([0.025, 0.025, 0.95, 0.95])
        plt.xticks([])
        plt.yticks([])
        plt.title("Rule {}".format(i))
        plt.imshow(cellularPattern)
        plt.pause(0.001)
