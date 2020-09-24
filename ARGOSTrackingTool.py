#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Sage Riddick (sage.riddick@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object =  open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Pretend we read one line of data
lineString = line_list[100]
#Split the string into a List of data items
lineData = lineString.split()

#Extract items in List into variables
record_id=lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData [6]
obs_long = lineData [7]

#Print location of sara
print(f"Record {record_id} Indicated Sara was seen at lat:{obs_lat}, lon:{obs_long} on {obs_date}")
