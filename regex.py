import re, argparse

def find(pat, text):
    searchResult = re.search(pat, text, re.M|re.I)
    # matchResult = re.match(pat, text, re.M|re.I)

    if searchResult:
        print("Found : " + searchResult.group())
    else:
        print("Not found!")

    

    # if matchResult:
    #     print("Match : " + matchResult.group())
    # else:
    #     print("Match not found!")


def main():

    # text = str(input("Enter short text : "))
    # pat = str(input("What are you looking for? : "))
    # # match = re.search("ing", "Human beign often such")
    # # print(match.group())
    # find(pat, text)

    parser = argparse.ArgumentParser()
    parser.add_argument('word', help="What word are you looking for")
    parser.add_argument('file', help="Enter a file name")
    parser.add_argument('-o', '--output', help="Save result into a file", action="store_true")


    args = parser.parse_args()

    file_ = open(args.file)
    lineNum = 0

    for line in file_.readlines():

        line = line.strip('\n\r')
        lineNum += 1

        searchResult = re.search(args.word, line, re.M|re.I)
        
        if searchResult:
            result = str(lineNum)+": "+line
            # print(result)
        # if not searchResult:
        #     print(line + " not found!")

            f = open("regex.txt", "a") ### 'w+': overwritten all file, 'r+': read a file, 'a': append data in file without crash previous data 
            f.write(result)
            f.close()

    file_.close()





if __name__== '__main__':
    main()