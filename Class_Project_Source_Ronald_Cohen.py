###################################################################################
# Class Project: Ron Cohen                                                        #
# Python, Fall Semester, 2018                                                     #
# GITHUB modify	001A  						                                      #
# Function: Text Parser:                                                          #
# Generates counts of chars, words, all whitespace chars, number "words"          #
# Occurrences and positions of consecutive whitespace chars, formatted numbers    #
# Import Modules:                                                                 #
# Regular Expressions (RE): text string pattern recognition                       #
# Collections (Collections): enhancing Python's list datatypes functionality      #
###################################################################################

import collections
import re

lline = input('Enter a Line>>> ')

print ('-----')
punc = [';',',','.','!','-','?','_','&','=','+','<','>']
words_ary = []
whsp_ary = []
nums_ary = []
dups_whsp_ary = []
ctr = 0
ctrws = 0
ctrnws = 0
ctrwd = 0
dblws = 0
ctrdlm = 0
uctr = 0
lctr = 0
nctr = 0
nums = 0
rewsp = 0
last_whsp_ctr = -1
last_nwhsp_ctr = -1
thisword = ''
thisnum = ''
#print (lline)

for i in lline:
    #print (i)
    ctr+=1
    if i.isupper():
        uctr+=1
    if i.islower():
        lctr+=1
    if i.isdigit():
        nctr+=1
    if i.isalpha():
        ctrnws+=1
        
    if re.match(r'\s', i):
        rewsp+=1    

    if (i in punc) or (re.match(r'\s',i)):

        ctrdlm+=1
        
        if i in (',','.') and last_ch.isdigit():
            #ctrnws+=1
            thisword = thisword + i
            last_ch = i
            #nctr-=1
            #print('new...',thisword)
        
        else:
           
            #print(thisword)
            if thisword != '':
                if thisword.isdigit():
                    nums+=1
                    nums_ary.append(thisword)
                else:
                    ctrwd+=1
                    words_ary.append(thisword)
            
            #print (words_ary)
            if re.match(r'\s',i):
                if ctr == last_whsp_ctr + 1:
                    dups_whsp_ary.append(last_whsp_ctr)
                    dblws+=1
                last_whsp_ctr = ctr

            thisword = ''
            thisnum = ''
        
    else:
        last_ch = i
        #print('Else...',thisword)
        thisword = thisword + i
    
if ctr > 0:
    if thisword != '':
        if thisword.isdigit():
            nums+=1
            nums_ary.append(thisword)
        else:
            ctrwd+=1
            words_ary.append(thisword)
    #print (words_ary)
    
print ('Total Words: ',ctrwd)
print ('Total Numbers: ',nums)
print ('Total Chars: ',ctr)
print ('Total Word Chars: ',ctrnws)
print ('Total Numeric Chars: ',nctr)
print ('Total Word Delimiter Chars: ',ctrdlm)
print ('Total Whitespace chars: ',rewsp)
print ('Total Uppercase Word Chars: ',uctr)
print ('Total Lowercase Word Chars: ',lctr)
print ('Total Occurrences of Consecutive WhiteSpace Chars: ',dblws)

if ctrnws > 0:
    print ('-----')
    print ('Words List Frequency:')
    cn = collections.Counter(words_ary)
    for k,v in cn.most_common():
        print(k,v)

if nctr > 0:
    cn = collections.Counter(nums_ary)
    if cn:
        print ('-----')
        print ('Numbers List Frequency:')
        for k,v in cn.most_common():
            print(k,v)

if dblws > 0:
    print ('-----')    
    print ('Occurrences of Consecutive Whitspace Chars at Position(s): ')
    for x in dups_whsp_ary:
        print(x)
