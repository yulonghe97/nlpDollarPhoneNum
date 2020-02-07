# NLP Program to identify telephone number in the txt file.
# @Author: Yulong He 2020.02.07
# Possible format to identify:
# 800-555-5555
# 215-470-4771
# (702) 798-2423
# 754-3010
# (541) 754-3010

import re
import sys

#  Open the text file with 16MB buffer to handle larger file


def main():

    with open(sys.argv[1], 'r', 16777216) as file:
        data = file.read()

    # regex expression to find telephone number
    regex_telephone = r"(\d{3}-\d{3}-\d{4})|(\(\d{3}\)\s\d{3}-\d{4})"

    telephone_list = []

    # Find the telephone number through iterator
    telephone_match = re.finditer(regex_telephone, data, re.MULTILINE)

    for matchNum, match in enumerate(telephone_match, start=1):
        telephone_list.append(match.group().strip('.,'))

    # Write list into the file
    with open('telephone_output.txt', 'w', 16777216) as writeList:
        writeList.writelines("%s\n" % word for word in telephone_list)

    print('Result Exported as telephone_output.txt')

    writeList.close()
    file.close()


main()
