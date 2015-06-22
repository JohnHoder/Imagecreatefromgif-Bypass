'''
A simple helper script to find byte sequences present in both of 2 given files. 
The main purpose of this is to find bytes that remain untouched after being processed with imagecreatefromgif()
PHP function from GD-LIB. That is the place where a malicious PHP script can be inserted to achieve some nasty RCE.

Date: March 2015
Jan Hodermarsky
'''

from __future__ import with_statement
import os, sys
import binascii

#Number of bytes we need for our malicious PHP code
size = 13

def filecmp(filename1, filename2):

    with open(filename1, "rb") as fp1, open(filename2, "rb") as fp2:

        #First file
        list1 = []
        byteSequence1 = fp1.read(size)

        while True:
            hexedBS1 = binascii.hexlify(byteSequence1)
            print hexedBS1

            list1.append(hexedBS1)

            fp1.seek(-size+1, 1)
            byteSequence1 = fp1.read(size)

            if fp1.read(1) == '':
                break
            fp1.seek(-1,1)

        
        #Second file
        list2 = []
        byteSequence2 = fp2.read(size)

        while True:
            hexedBS2 = binascii.hexlify(byteSequence2)
            print hexedBS2

            list2.append(hexedBS2)

            fp2.seek(-size+1, 1)
            byteSequence2 = fp2.read(size)

            if fp2.read(1) == '':
                break
            fp2.seek(-1,1)

        #Output results
        print "\n"
        
        print "Count of " + str(size) + "-byte sequences in 1st file: " + str(len(list1))
        print "Count of " + str(size) + "-byte sequences in 2nd file: " + str(len(list2)) + "\n"

        print "\nMatches:\n"

        matchSet = (set(list1) & set(list2))
        for match in list(matchSet):
            print match

        return

if __name__ == "__main__":
    if(len(sys.argv) == 3):
        filecmp(sys.argv[1], sys.argv[2])
    else:
        print "Provide the proper number of arguments.\n"
        print "Syntax:"
        print sys.argv[0] + " file1 file2\n"
