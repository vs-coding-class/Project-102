import os

def openIndividual(path):
    os.system(f'open {path}')
    print('Application is opened.')

def openMultipleApplications(listName):
    file = open('Application_Lists.txt', 'r')
    for line in file:
        names = line.split(', ')
        if names[0] == listName:
            for item in names[1:]:
                os.system(f'open {item}')

def main():
    while True:
        type = input("Please enter 'one' to open only one application or 'list' to open a set of applications: ")
        if type == 'one':
            oneFile = input('Please enter the name of the application you would like to open: ')
            openIndividual(oneFile)
        elif type == 'list':
            setName = input('Please enter the name of the set of applications you would like to open: ')
            openMultipleApplications(setName)
        else:
            print('Please enter a response that is compatible with the program.')

main()
