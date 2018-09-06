import os, sys
import re
import vim

def main():
    fileName = vim.current.buffer.name
    print('Generating test file for ' + fileName)
    testFileName = fileName[:-3] + "_test.go"
    fileContents = _getFileContents(fileName)
    if _fileExists(testFileName) is False:
        packageName = _getPackage(fileContents)
        _createTestFile(testFileName, packageName)

    
    testFileContents = _getFileContents(testFileName)
    mainFunctions = _arrayOfAllFunctions(fileContents)
    testFuncitons = _arrayOfAllFunctions(testFileContents)

    functionsToBeCreated = []
    for functionName in mainFunctions:
        if functionName not in _originalName(testFuncitons):
            functionsToBeCreated.append(_createTestFunction(functionName))

    _appendFunctions(testFileName, functionsToBeCreated)
    print('Done... ')

def _originalName(testFunctionNames): 
    names = [testFunctionName.split('Test')[1] for testFunctionName in testFunctionNames]
    return names

def _createTestFunction(functionName):
    return "Test" + functionName

def _appendFunctions(testFileName, functionsToBeCreated):
    f = open(testFileName, "a")
    for fn in functionsToBeCreated:
        f.write("\nfunc " + fn + " (t *testing.T) {\n\n}\n")
    f.close()


def _getFileContents(fileName):
    fileContents = ""
    f = open(fileName, "r")
    fileContents = f.read()
    f.close()
    return fileContents


def _fileExists(fileName):
    return os.path.isfile(fileName)


def _getPackage(fileContents):
    pattern =  re.compile("[\n]?package(.*)")
    packageName = pattern.findall(fileContents)[0]
    return packageName.strip()


def _createTestFile(fileName, packageName="vector"):
    f = open(fileName, "w")
    f.write("""package """)
    f.write(packageName)
    f.write("\n\nimport (\n\t\"testing\"\n)\n")
    f.close()


def _arrayOfAllFunctions(contents):
    functionPattern = re.compile('func\s*(\([\w\s*]*\))?\s*(\w*)[\s(]*')
    functionSignatures = functionPattern.findall(contents)
    functionNames = []
    for sign in functionSignatures:
        functionNames.append(sign[1].strip())
    return functionNames

def hello():
    print("Hello World")
