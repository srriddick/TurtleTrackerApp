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

#Ask user for the search date
user_date = input("Enter date to search for Sara: ")

#Create a variable pointing to the data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object =  open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two empty dictionary objects
date_dict = {}
coord_dict = {}

#Interate through all lines in the lineList
for lineString in line_list:
    if lineString[0] == "#" or lineString[0] == "u" : continue
    #Split the string into a List of data items
    lineData = lineString.split()
    
    #Extract items in List into variables
    record_id=lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    #if obs_lc not in ("1", "2", "3"):
        #continue
    obs_lat = lineData [6]
    obs_long = lineData [7]
    
    #Print location of sara if lc is 1, 2, or 3
    if obs_lc in ("1","2","3"):
        #print(f"Record {record_id} Indicated Sara was seen at lat:{obs_lat}, lon:{obs_long} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_long)

#Create empty list to hold matching keys
matching_keys = []

#Loop through items in the date_dict, and collect keys for matching ones 
for date_item in date_dict.items():
    #Get the date of the item
    the_key, the_date = date_item
    #See if the date matches the user date
    if the_date == user_date:
        #If so, add the key to the list
        matching_keys.append(the_key)
        
#Reveal locations for each key in matching_keys
for matching_key in matching_keys:
    obs_lat, obs_long = coord_dict[matching_key]
    print(f"Record {matching_key} Indicated Sara was seen at lat:{obs_lat}, lon:{obs_long} on {user_date}")
        