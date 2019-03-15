# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 12:45:41 2016

@author: simon.desmet
"""

# read in a csv file, 
#identify line 1 of the time series data,
# ask user for current time step and desired timestep
#delete additional timesteps (rows) down to desired timestep - auto save output

#if possible do it entirely in CORE.



import os # a module that allows os commands
import glob # a module that allows python to recognise specific file extentions

#-----------------------------------------------------------------------


PATH1 = raw_input("folder containing CSVs path please:") 


inputlistB = []

    
for filename in glob.glob(os.path.join(PATH1, '*.csv')):
    print filename
    inputlistB.append(filename)
    
print inputlistB







#PATH1 = raw_input("file path please:")


 

#INPUTPATH = PATH1




# asks user for new time step and converts to float.



#-----------------------------------------------------------------------


firstline = raw_input("what line do you want to start at?:")
lastline = raw_input("What line do you want to end / clip at?")

startline = int(firstline)
endline = int(lastline)

print startline
print endline
# asks for starting line for process, and converts it to an integer.



#-----------------------------------------------------------------------

# now we determine how what lines need to be deleted

# takes the new time step then divides it by the old to get the line number we want to save.
# we then create a new list of lines from the old but only with the lines of thi





#-----------------------------------------------------------------------

# now we read in the file & operate
for CSV in inputlistB:
    with open(CSV) as f: # open the file at our input path
        content = f.readlines() # read file into variable content

    
    lines = list(content)
    print startline

    newlines = lines[startline:endline] # copys every X line into new list called newlines, where x is our saveno line that we want to keep
    print newlines
    finallines = newlines #new list that sticks our header to our new timestep lines
    

            


#-----------------------------------------------------------------------

# now we write the output.

#for inputfile in inputlistB: # creates new varible 'inputfile' from each item in list inputlistB
 #   with open(inputfile) as f: # with - so does what follows with this line in effect, opens file as f
#        content =f.readlines() # creates new varible 'content' and reads entire file into it.
  #      print content

    ppos = CSV.index('.')


    PATHA = CSV[0:ppos]
    PATHB = CSV[ppos:]

    OUTPUTPATH = PATHA+'output'+PATHB

    output = open(OUTPUTPATH,'w')
    for line in finallines:
        output.write(line)

output.close()
