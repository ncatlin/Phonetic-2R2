#!/usr/bin/python
'''
Created on 10 Apr 2014

@author: Nia Catlin
'''

import sys
    
if __name__ == '__main__':
    
    equivalents = {1:['A','E','I','O','U'],
                   2:['C','G','J','K','Q','S','X','Y','Z'],
                   3:['B','F','P','V','W'],
                   4:['D','T'],
                   5:['M','N']}
    
    #reduce the name supplied to a string describing its equivalent sets
    def reduceName(name):
        
        #rule 1: discard non alphabetic characters
        name = ''.join(i for i in name if i.isalpha()) 
        
        if len(name) == 0: return ''
        
        name = name.upper() #rule 2: ignore case
        
        #rule 3: discard certain letters after the first
        name = name[0] + name[1:].translate(None,'AEIHOUWY') 
        
        #rule 4: consider certain sets of letters equivalent
        activeSet = 0
        reducedName = ''
        for character in name:
            #rule 5: consecutive members of set are single occurrence
            if activeSet != 0 and character in equivalents[activeSet]: continue 
            
            for setID,charset in equivalents.items():
                if character in charset:
                    reducedName += str(setID)
                    activeSet = setID
                    break
            else:
                reducedName += character
                activeSet = 0
        
        return reducedName  
    
    #build a reduced name -> real name dictionary from the supplied list
    inputNameDict = {} 
    for name in sys.stdin.readlines():
        name = name.strip()
        reducedName = reduceName(name)
        if reducedName not in inputNameDict:
            inputNameDict[reducedName] = name
        else: inputNameDict[reducedName] += ', '+name
    
    #check supplied names against that dictionary     
    for name in sys.argv[1:]:
        reducedName = reduceName(name)
        if reducedName in inputNameDict: print '\n%s: %s'%(name,inputNameDict[reducedName])
