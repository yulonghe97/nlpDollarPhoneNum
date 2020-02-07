# NLP Program to identify dollar amount in the txt file, it will output the dollar amount included in the txt file
# @Author: Yulong He 2020.02.07
# Possible format for identification:
# $500 million/billion/trillion
# $6.57
# 1 dollar and 7 cents
# 5 cent/cents
# one/two/three hundred/hundreds/million/billion... dollar/dollars

import re
import sys


#  Open the text file with 16MB buffer to handle larger file


def main():

    with open(sys.argv[1], 'r', 16777216) as file:
        data = file.read()

    # regex word expression:
    # ([\d]*\sdollar\sand\s[\d]*\scents)|
    # ([\d]*\sdollars\sand\s[\d]*\scents)|
    # ([\d]*\sdollar\sand\s[\d]*\scent)|
    # ([\d]*\sdollars\sand\s[\d]*\scent)|
    # (^\$?[\d]*\smillion)|
    # (^\$?[\d]*\sbillion)|
    # (^\$?[\d]*\stillion)|
    # (^\$?[\d]{0,2}\sdollar)|
    # (^\$?[\d]{0,2}\sdollars)|
    # (^\$?[\d]*\scents)|
    # (^\$?[\d]*\scent)|
    # ((\bone\b|\btwo\b|\bthree\b|\bfour\b|\bfive\b|\bsix\b|\bseven\b|\beight\b|\bnine\b)+\s+(hundred|thousand|million|billion|trillion)+\s+(dollars|dollar))

    regex_word = r"([\d]*\sdollar\sand\s[\d]*\scents)|([\d]*\sdollars\sand\s[\d]*\scents)|([\d]*\sdollar\sand\s[\d]*\scent)|([\d]*\sdollars\sand\s[\d]*\scent)|(^\$?[\d]*\smillion)|(^\$?[\d]*\sbillion)|(^\$?[\d]*\stillion)|(^\$?[\d]{0,2}\sdollar)|(^\$?[\d]{0,2}\sdollars)|(^\$?[\d]*\scents)|(^\$?[\d]*\scent)|((\bone\b|\btwo\b|\bthree\b|\bfour\b|\bfive\b|\bsix\b|\bseven\b|\beight\b|\bnine\b)+\s+(hundred|thousand|million|billion|trillion)+\s+(dollars|dollar))"

    # regex number expression:
    regex_numbers = r"(\$\s?([\d]*[,]?){0,}[.]?[\d]{0,2})"

    test_str = data
    testStrWordEliminatedList = []
    dollarNumbersList = []
    testStrWordEliminated = test_str

    # Match for dollar, dollars, cent, cents, million, billion, trillion
    matches_word = re.finditer(regex_word, test_str, re.MULTILINE)

    for matchNum, match in enumerate(matches_word, start=1):
        testStrWordEliminatedList.append(match.group().strip('.,'))

    # Eliminate the noise from previous match
    for i in testStrWordEliminatedList:
        testStrWordEliminated = testStrWordEliminated.replace(i, '1')

    # Find the numeric numbers, including dollar sign.
    matches_numbers = re.finditer(regex_numbers, testStrWordEliminated, re.MULTILINE)

    for matchNum, match in enumerate(matches_numbers, start=1):
        dollarNumbersList.append(match.group().strip('.,'))

    # Combine two lists
    resultList = testStrWordEliminatedList + dollarNumbersList

    # Clean up Invalid results
    for i in resultList:
        if i == '$':
            resultList.remove('$')
        if i == '$ ':
            resultList.remove('$ ')
        if i == '$\n':
            resultList.remove('$\n')

    # Write list into the file
    with open('dollar_output.txt', 'w', 16777216) as writeList:
        writeList.writelines("%s\n" % word for word in resultList)

    print('Result Exported as dollar_output.txt')

    writeList.close()
    file.close()


main()
