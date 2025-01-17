# main
# Import Statements
from genericpath import isdir, isfile
from posixpath import dirname
import sys
import getopt
import os
import fnmatch
import shutil

# Global Variables
workingDirectoryPath = os.getcwd()
distFolder = workingDirectoryPath + "/dist"
arrayOfFiles = []
arryOfFilesWithExtension = []
secondArg = ""
isCustomDirectory = False
customDirectoryPath = ""
fileName = ""
dirName = ""
# Functions
# Converting txt files
def conversionFuncFile():
    # Local Variables
    localArrOfFiles = []
    striclyFileNames = []
    fileCounter = 0
    for i in arrayOfFiles:
        striclyFileNames.append(i)
        if os.name == "posix":
            temp = os.getcwd() + "/" + str(i)
        else:
            temp = os.getcwd() + "\\" + str(i)

        localArrOfFiles.append(temp)
    print("\n~~~ SSG Compiling and Working! ~~~\n")
    # For File name convert into html and create new File.
    if isCustomDirectory is False:
        try:
            if os.path.isdir(
                "dist"
            ):  # Check to see if dist exists, if it does, delete children and parent
                shutil.rmtree(distFolder)
            os.mkdir(distFolder)  # Try to create new dist folder
        except OSError as error:
            print("\n--- FAILURE ---")
            print(error)

        for aFile in localArrOfFiles:
            originalFile = open(aFile, "r", encoding="utf8")  # Read existing file
            os.chdir(distFolder)  # Change directories
            originalFileName, end = os.path.splitext(
                striclyFileNames[fileCounter]
            )  # Cut off the extension of the file

            newFile = open(
                originalFileName + ".html", "w"
            )  # Create new File under html extension
            newFile = open(
                originalFileName + ".html", "a"
            )  # Open file to append contents

            newFile.write("<!doctype html>\n")
            newFile.write('<html lang="en">\n')
            newFile.write("<head>\n")
            newFile.write('\t<meta charset="utf-8">\n')
            newFile.write("\t<title>" + originalFileName + "</title>\n")
            newFile.write(
                '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            )
            newFile.write("</head>\n")
            newFile.write("<body>\n")

            temp = originalFile.read().splitlines()

            for x in temp:  # Loop through the file we opened
                if x != "":  # We dont want <p> tags created for new lines
                    if end == ".txt":
                        newFile.write("\t<p>" + x + "</p>\n")
                    if end == ".md":
                        if x.startswith("# "):
                            x = x.replace("# ", "<h1>")
                            newFile.write("\t" + x + "</h1>\n")
                        else:
                            newFile.write("\t<p>" + x + "</p>\n")
            newFile.write("</body>\n")
            newFile.write("</html>")
            fileCounter += 1
            originalFile.close()
            newFile.close()
        print("\n--- SUCCESS ---")
    else:
        for aFile in localArrOfFiles:
            originalFile = open(aFile, "r", encoding="utf8")  # Read existing file
            os.chdir(customDirectoryPath)  # Change directories
            originalFileName = os.path.splitext(striclyFileNames[fileCounter])[
                0
            ]  # Cut off the extension of the file

            newFile = open(
                originalFileName + ".html", "w"
            )  # Create new File under html extension
            newFile = open(
                originalFileName + ".html", "a"
            )  # Open file to append contents

            newFile.write("<!doctype html>\n")
            newFile.write('<html lang="en">\n')
            newFile.write("<head>\n")
            newFile.write('\t<meta charset="utf-8">\n')
            newFile.write("\t<title>" + originalFileName + "</title>\n")
            newFile.write(
                '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            )
            newFile.write("</head>\n")
            newFile.write("<body>\n")

            temp = originalFile.read().splitlines()

            for x in temp:  # Loop through the file we opened
                if x != "":  # We dont want <p> tags created for new lines
                    newFile.write("\t<p>" + x + "</p>\n")
            newFile.write("</body>\n")
            newFile.write("</html>")
            originalFile.close()
            fileCounter += 1
            newFile.close()
            print("\n--- SUCCESS ---")


# Converting files from within a folder
def conversionFuncFolder():
    # Local Variables
    localArrOfFiles = []
    striclyFileNames = []
    fileCounter = 0
    counter = 1
    previousFileNameArr = []
    print("\n~~~ SSG Compiling and Working! ~~~\n")
    if isCustomDirectory == False:  # Check to see if a custom output directory exists.
        try:
            if os.path.isdir(
                "dist"
            ):  # Check to see if dist exists, if it does, delete children and parent
                shutil.rmtree(distFolder)
        except OSError as error:
            print("\n--- FAILURE ---")

        # Try to create new dist folder
        os.mkdir(distFolder)
        # Change to specified Folder
        os.chdir(dirName)
        # Gather local files and convert them into usable paths
        for i in arrayOfFiles:
            striclyFileNames.append(i)
            temp = os.getcwd() + "\\" + str(i)
            localArrOfFiles.append(temp)

        # Main Logic
        for (
            aFile
        ) in (
            localArrOfFiles
        ):  # For each file name convert into html and create new file.
            originalFile = open(
                aFile, "r", encoding="utf8"
            )  # Open for reading the existing file
            originalFileName = os.path.splitext(striclyFileNames[fileCounter])[
                0
            ]  # Cut off the extension of the file
            previousFileNameArr.append(originalFileName)

            os.chdir(distFolder)

            # Creating the new file template
            newFile = open(
                originalFileName + ".html", "w"
            )  # Create new File under html extension
            newFile = open(
                originalFileName + ".html", "a"
            )  # Open file to append contents
            newFile.write("<!doctype html>\n")
            newFile.write('<html lang="en">\n')
            newFile.write("<head>\n")
            newFile.write('\t<meta charset="utf-8">\n')
            newFile.write("\t<title>" + originalFileName + "</title>\n")
            newFile.write(
                '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            )
            newFile.write("</head>\n")
            newFile.write("<body>\n")
            newFile.write('<a href="./index.html">Back to Home</a>')

            temp = (
                originalFile.read().splitlines()
            )  # Read through the original file and remove line breaks
            for x in temp:  # Loop through the file we opened
                if x != "":  # We dont want <p> tags created for new lines
                    newFile.write("\t<p>" + x + "</p>\n")
            newFile.write("</body>\n")
            newFile.write("</html>")
            originalFile.close()
            newFile.close()
            fileCounter += 1
            os.chdir(dirName)

        # Create Custom Index html page with links to all the created files
        print("Creating HTML file")
        os.chdir(distFolder)
        indexPage = open("index.html", "w")
        indexPage.write("<!doctype html>\n")
        indexPage.write('<html lang="en">\n')
        indexPage.write("<head>\n")
        indexPage.write('\t<meta charset="utf-8">\n')
        indexPage.write("\t<title>" + "Index" + "</title>\n")
        indexPage.write(
            '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        )
        indexPage.write("</head>\n")
        indexPage.write("<body>\n")
        for name in previousFileNameArr:
            linkString = f'<a href="./{name}.html">{counter}. {name}</a><br>'
            indexPage.write(str(linkString))
            counter += 1
        indexPage.close()
        print("\n--- SUCCESS ---")
    else:
        # Change to specified Folder
        os.chdir(dirName)
        # Gather local files and convert them into usable paths
        for i in arrayOfFiles:
            striclyFileNames.append(i)
            temp = os.getcwd() + "\\" + str(i)
            localArrOfFiles.append(temp)

        # Main logic
        for aFile in arrayOfFiles:
            # os.chdir(dirName)
            originalFile = open(
                aFile, "r", encoding="utf8"
            )  # Read current existing file
            os.chdir(customDirectoryPath)  # Change directories
            aFile = os.path.splitext(aFile)[0]  # Cut off the extension of the file
            previousFileNameArr.append(aFile)

            # Creating the new file template
            newFile = open(aFile + ".html", "w")  # Create new File under html extension
            newFile = open(aFile + ".html", "a")  # Open file to append contents
            newFile.write("<!doctype html>\n")
            newFile.write('<html lang="en">\n')
            newFile.write("<head>\n")
            newFile.write('\t<meta charset="utf-8">\n')
            newFile.write("\t<title>" + aFile + "</title>\n")
            newFile.write(
                '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            )
            newFile.write("</head>\n")
            newFile.write("<body>\n")
            newFile.write('<a href="./index.html">Back to Home</a>')

            temp = (
                originalFile.read().splitlines()
            )  # Read through the original file and remove line breaks
            for x in temp:  # Loop through the file we opened
                if x != "":  # We dont want <p> tags created for new lines
                    newFile.write("\t<p>" + x + "</p>\n")
            newFile.write("</body>\n")
            newFile.write("</html>")

            originalFile.close()
            newFile.close()
            os.chdir(dirName)

        # Create Custom Index html page with links to all the created files
        os.chdir(customDirectoryPath)
        indexPage = open("index.html", "w")
        indexPage.write("<!doctype html>\n")
        indexPage.write('<html lang="en">\n')
        indexPage.write("<head>\n")
        indexPage.write('\t<meta charset="utf-8">\n')
        indexPage.write("\t<title>" + "Index" + "</title>\n")
        indexPage.write(
            '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        )
        indexPage.write("</head>\n")
        indexPage.write("<body>\n")
        for name in previousFileNameArr:
            linkString = f'<a href="./{name}.html">{counter}. {name}</a><br>'
            indexPage.write(str(linkString))
            counter += 1
        indexPage.close()
        print("\n--- SUCCESS ---")


# Main Logic
if __name__ == "__main__":
    short_opts = "hiov"
    long_opts = ["help", "input=", "output=", "version"]
    temp = sys.argv
    arguments = temp[1:]
    try:
        arg, values = getopt.getopt(arguments, short_opts, long_opts)
    except getopt.error as error:
        print(error)
    if len(arg) == 0:
        print("Run Help command using -h or --help")
    else:
        for curr_arg, curr_value in arg:
            if curr_arg in ("--version", "-v"):
                print("Welcome to the RomanStaticSG, a Static Site Generator")
                print("The current version is: 0.1")
            elif curr_arg in ("--help", "-h"):
                print("\nHelp Screen\n")
                print("Usage: python romanssg.py\n")
                print(
                    "Commands: \nTo get version number use the command: --version, -v"
                )
                print(
                    "To change the output directory to a user specified directory, run --output= or -o="
                )
                print(
                    "To specify an input, use either a file or a folder with items inside of it"
                )
                print("To specify input use: --input= or -i=")
            elif curr_arg in ("--output", "-o"):
                if os.path.isdir(curr_value):
                    print("Output Directory has been changed to " + curr_value)
                    isCustomDirectory = True
                    customDirectoryPath = curr_value
                else:
                    print(
                        "ERROR: Directory does not exist! Please enter a valid directory"
                    )
            elif curr_arg in ("--input", "-i"):
                if os.path.isdir(curr_value):
                    print("Working on Directory")
                    dirName = curr_value
                    for i in os.listdir(curr_value):
                        if fnmatch.fnmatch(i, "*.txt"):
                            arrayOfFiles.append(i)
                        if fnmatch.fnmatch(i, "*.md"):
                            arrayOfFiles.append(i)
                    conversionFuncFolder()
                else:
                    print("Working on File " + curr_value)
                    fileName = curr_value
                    # for i in os.listdir("."):
                    # if fnmatch.fnmatch(i, "[example]"):
                    #     print("matched with")
                    arrayOfFiles.append(fileName)
                    # if fnmatch.fnmatch(i, "*.md"):
                    #     arrayOfFiles.append(i)
                    conversionFuncFile()
            else:
                print("Error")
