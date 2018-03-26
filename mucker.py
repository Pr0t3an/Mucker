#!/usr/bin/python2.7

import base64
import zlib
import os
import re


def main():
    test2()
    #base64gzip()


def test2():
    with open('bla.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')
        print "=========================================="
        print "            Original Command Line         "
        print "=========================================="
        print "Original Length: " + str(len(data)) + "\n"
        print data

        #remove ^ first
        holdingstring = data.replace("^", "")
        #remove whitespace
        holdingstring = re.sub(' +', ' ', holdingstring)
        #convert case
        holdingstring = holdingstring.lower()
        # remove '( , '
        holdingstring = holdingstring.replace("( , ", "")
        # remove ' , )"
        holdingstring = holdingstring.replace(" , )", "")
        # extract set commands between brackets into list
        match = re.findall('\(set [^\=]{1,}=[^\&]{1,}', holdingstring)
        # remove those strings from the cmdline
        x = 0
        while x <len(match):
            holdingstring = holdingstring.replace(match[x], "")
            x += 1

        # remove the unwanted chars from our assignments
        match = [s.replace("(set ", "") for s in match]
        match = [s.strip(')') for s in match]

        # remove set commands matched from the string
        holdingstring = re.sub("\(set [^\=]{1,}=[^\&]{1,}'", "", holdingstring)
        #loop through the holding string and replace from list
        i = 0
        while i < len(match):
            holdingstring = holdingstring.replace(match[i].split('=')[0], match[i].split('=')[1])
            i += 1

        #Futher regex match on other set
        newmatch = re.findall('set [^\=]{1,}=[^\&]{1,}', holdingstring)
        y = 0
        while y < len(newmatch):
            holdingstring = holdingstring.replace(newmatch[y], "")
            y+=1
        newmatch = [s.replace("set ", "") for s in newmatch]

        z = 0
        while z < len(newmatch):
            holdingstring = holdingstring.replace(newmatch[z].split('=')[0], newmatch[z].split('=')[1])
            z += 1

        # tidy rest of the string
        #remove commas
        holdingstring = holdingstring.replace(",", "")
        # remove all calls
        holdingstring = holdingstring.replace("call", "")
        #remove remaining vars
        holdingstring = holdingstring.replace("%", "")
        holdingstring = holdingstring.replace("echo", "")
        # remove greater spaces where more than 1 exists
        holdingstring = holdingstring.replace("&", "")
        holdingstring = holdingstring.replace(" (", "")
        holdingstring = holdingstring.replace(") ", "")
        holdingstring = holdingstring.replace(");", "")
        holdingstring = holdingstring.replace(" ;", "")
        holdingstring = holdingstring.replace(" ;", "")
        holdingstring = holdingstring.replace(" ;", "")

        holdingstring = re.sub(' +', ' ', holdingstring)
        print "\n\n"
        print "=========================================="
        print "            Partial Command Line          "
        print "=========================================="
        print "Original Length: " + str(len(holdingstring)) + "\n"
        print holdingstring


def base64gzip():
    coded_string="H4sIAJCntloA/11Sy27VMBDd+ytm10QKH8ECQcQCCZAqlr7xxLbieIwfrcLX9zi5LYVNlDmZ85hz789noRRaoYoXX2iVlifafQQkkak6XR/w1WXmiX43v2y06+qK+vTE+TD6wBixIRFLTLcgyzZR2WUDGaSifjDTAVmyPgfy117SGWtd/Q4X0tSWjXNRj46vpeqjpWeOFcZ62T68e05dslvje2YyoPbl4RXtAJtRfZFgoGNdnehjiYgy7AfdssB6nMgxolupV6a2p4OGm7en879ksLpuZ9t2/E9dsy83ZjXjZp1w2NvztZjkUCdk5MnHh+vwRXJcg97Q0Xe/MH2FSPJcoP1m3H17QRM9Ol8jIx+Qz6P6dslm0YaMnJq9Nen04FE+1vpEw/tpVL/uBVUnrevPyC5/kGymgnY0JUaPlyUMIvAkBbUtzgfYjGpeqcBZY6j9Oo92ZrJOCl6cdvAX2QgHnr96vLMZ/5y/wKr3K4uR2MA7wSCwPuNanQ28ockvA0z1rqICAAA=="
    decoded_string = base64.b64decode(coded_string)
    decompressed_data=zlib.decompress(decoded_string, 16+zlib.MAX_WBITS)
    print decompressed_data

def test1():
    with open('bla.txt', 'r') as myfile:
        data = myfile.read().replace('\n', '')
        print "=========================================="
        print "            Original Command Line         "
        print "=========================================="
        print "Original Length: " + str(len(data)) + "\n"
        print data
        remove_carrot = data.replace("^", "")
        #print len(remove_carrot)
        remove_multispace = re.sub(' +', ' ', remove_carrot)
       # print len(remove_multispace)
        remove_case = remove_multispace.lower()
        remove_commasemi = remove_case.replace(", ; ,", "")
        remove_commasemi = remove_commasemi.replace(", ;", "")
        remove_commasemi = remove_commasemi.replace("; ,", "")
        remove_commasemi = remove_commasemi.replace(", ,", "")
        # remove_commasemi = remove_commasemi.replace(";", "")
        remove_commasemi = re.sub(' +', ' ', remove_commasemi)
        remove_commasemi = remove_commasemi.replace("& ", "&")
        remove_commasemi = remove_commasemi.replace("( (", "((")
        remove_commasemi = remove_commasemi.replace(" , ", ",")
        remove_commasemi = remove_commasemi.replace(") )", "))")
        remove_commasemi = remove_commasemi.replace(",,,", "")
        # print remove_commasemi
        # print len(remove_commasemi)
        #remove_commasemi = re.sub(' +', ' ', remove_commasemi)
        #print len(remove_commasemi)
        remove_doublequotes = remove_commasemi.replace('""', '')

        #\(, \(set [^\=]{1,}=[^\&]{1,}&&
        new = re.sub('\(, \(set [^\=]{1,}=[^\&]{1,}&&', "", remove_doublequotes)
        new = re.sub('\(set [^\=]{1,}=[^\&]{1,}&&', "", new)
        new = re.sub('\(set [^\=]{1,}=[^\&]{1,}&', "", new)
         #regex = \(set [^\=]{1,}=[^\&]{1,}
        match = re.findall('\(set [^\=]{1,}=[^\&]{1,}', remove_doublequotes)
        remove_listchar = [s.replace("(set ", "") for s in match]
        remove_listchar = [s.replace("set ", "") for s in remove_listchar]
        remove_listchar = [s.strip(')') for s in remove_listchar]

        new = new.replace("(,( ,(((,((, ((((;; call ;; ", "")
        #print new
        i = 0
        while i < len(remove_listchar):
            new = new.replace(remove_listchar[i].split('=')[0], remove_listchar[i].split('=')[1])
            i += 1
        i = 0
        #print new
        new = new.replace('%', '')
        #print new
        new = new.replace('),', '')
        #print new
        new = new.replace('; ', '')
        #print new
        new = new.replace(') ', '')
        new = new.replace('c a', 'ca')
        print new
        print "\n"
        print "=========================================="
        print "   Partial De-obfuscuated Command Line    "
        print "=========================================="
        print "New Length: " + str(len(new)) + "\n"
        print new + "\n\n"


if __name__ == "__main__":
    main()
