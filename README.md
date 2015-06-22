# Imagecreatefromgif-Bypass

A simple helper script to find byte sequences present in both of 2 given files. 
The main purpose of this is to find bytes that remain untouched after being processed with imagecreatefromgif()
PHP function from GD-LIB. That is the place where a malicious PHP script can be inserted to achieve some nasty RCE.

Date: March 2015
Jan Hodermarsky
