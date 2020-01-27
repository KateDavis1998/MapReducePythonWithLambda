#Kate Davis - Lab 1

#My input list
inputList = [35, 45, 30, 30, 45, 23, 38, 43, 48, 50, 50, 67, 24, 3, 1]

#Placeholders for hash map
finalOutput = {}
finalLambdaOutput = {}

#Regular Map Func
def mapReg(index, value):
    mapop = []
    for number in inputList:
        check = evenOrOdd(number)
        if check == True:
            temp = ('Even', 1)
        else:
            temp = ('Odd', 1)
        mapop.append(temp)
    return mapop

#Check if even or odd
def evenOrOdd(value):
    if(value % 2) == 0:
        return True
    else:
        return False

#Reduce the map
def reduceReg(index, value):
    if index not in finalOutput:
        finalOutput[index] = 0
    finalOutput[index] += 1

#Main
if __name__ == '__main__':

    #Map and Reduce without lambda
    map_output = []
    map_output = mapReg(0, inputList)
    
    print('Regular Output')
    print(map_output)
    
    for k, v in map_output:
        reduceReg(k, v)
        
    print(finalOutput)
    
    print('Lambda Outout')

    #Map and Reduce with lambda
    mapLambda = lambda k,v: [('Odd', 1) if (number % 2 != 0) else ('Even', 1) for number in inputList]
    reduceLambda = lambda k: 0 if k not in finalLambdaOutput else finalLambdaOutput[k]

    #Make Dict and Fill using Lambda
    dict_x = []
    dict_x = mapLambda(0, inputList)
    print(dict_x)
    
    #Reduce the Dict
    for k, v in dict_x:
        finalLambdaOutput[k] = reduceLambda(k)
        finalLambdaOutput[k] += 1

    print(finalLambdaOutput)
