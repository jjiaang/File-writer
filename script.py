def getUserInput():
    print("Enter the name of the input file")
    fileName = input()
    return fileName

def specifyOutputFile():
    print("Enter the name of the output file")
    outputFile = input()
    return outputFile

def getUserInput2():
    print("How many times?")
    count = input()
    return count

def fileReadWrite(inputFile,count,outputFile):
    newArray = []
    with open(inputFile) as f:
        aList = [line.rstrip() for line in f]
    
    aList = [int(i) for i in aList]

    for i in range(len(aList)):
        for j in range(len(aList)):
            if j == 0:
                for x in range(int(count)):
                    newArray.append(aList[i] + x)
    newArray = list(map(str, newArray))
    with open(outputFile, 'w') as f:
        for item in newArray:
            f.write("%s\n" % item)
    print("Content written in " + outputFile)

def main():
    inputFile = getUserInput()
    outputFile = specifyOutputFile()   
    count = getUserInput2()
    fileReadWrite(inputFile,outputFile,count)

main()