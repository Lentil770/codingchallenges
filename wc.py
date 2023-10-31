import sys, re

def calculateBytesInFile(filepath):
    with open (filepath,'rb') as f:
        return len(f.read())
    

def calculateLinesInFile(filepath):
    # dont know why its only working with bytes
    with open (filepath, 'rb') as file_object:
        lineCount=0
        for line in file_object:
            lineCount=lineCount+1
        return lineCount
        
def calculateWordsInFile(filepath):
    with open(filepath, encoding="utf8") as fp:
        words = fp.read().split()
        return len(words)
    

def calculateCharactersInFile(filepath):
    with open (filepath,encoding="utf8" ) as file:
        return len(file.read())
    # returning less than wc -m, possibly bc counting unicode chars not bytes?
        



# wc test.txt==  6667  58164 343624 test.txt

# runs file with arguments
if sys.argv[1] == '-c': # count file bytes
    print(calculateBytesInFile(sys.argv[2]), sys.argv[2])
if sys.argv[1] == '-l': # count file lines
    print(calculateLinesInFile(sys.argv[2]), sys.argv[2])
if sys.argv[1] == '-w': # count file words
    print(calculateWordsInFile(sys.argv[2]), sys.argv[2])
if sys.argv[1] == '-m': # count file characters
    print(calculateCharactersInFile(sys.argv[2]), sys.argv[2])
if sys.argv[1] and sys.argv[2]=='':
    print(calculateBytesInFile(sys.argv[1]), calculateLinesInFile(sys.argv[1]),calculateWordsInFile(sys.argv[1]),  sys.argv[1])

if sys.argv[1]=='' and sys.argv[2]=='':
    print(sys.stdin)

# [COMPLETE] Step 1 - -c
# [COMPLETE] step 2 - -l
# [COMPLETE] step 3 -w
# [ISH COMPLETE] step 4 -m
# [COMPLETE] step 5 default (== -c -l -w)
# step 6 ?