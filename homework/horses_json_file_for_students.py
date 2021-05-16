# This file contains your entire homework.
# 2CR students start from the top and work until you see the 4CR mark.
# 4CR students complete all problems.
# There is a 4CR only discussion problem earlier on, watch for the note!
# Narratives are expected as normal for problems as marked.

#####################################################
# I'm providing the two helper functions from class #
# Do not change either of these.                    #
#####################################################

def get_id_from_url(url_string):
    '''pass this a string with a wikidata url
       it will return just the id from that url'''
    if url_string == 'missing':
        wikidataid= 'missing'
    else:
        parts = url_string.split('/')
        wikidataid = parts[-1]
    return wikidataid

def clean_missing(key, record):
    '''function will check if a provided key is inside a record
    and return either that value or the string value of missing.'''
    if key in record:
        result = record[key]
    else:
        result = 'missing'
    return result

########################
# Discussion problem 1 # (no narrative expected)
########################
# here's an example of a single horse entry for reference:

"""
{
	"horse": "http://www.wikidata.org/entity/Q1001792",
	"horseLabel": "Makybe Diva",
	"mother": "http://www.wikidata.org/entity/Q14949904",
	"father": "http://www.wikidata.org/entity/Q5263956",
	"birthyear": "1999",
	"genderLabel": "female organism"
}"""

# Can you think of exploration or analysis questions you might want to ask this dataset?
# Write three below (you can write these either in this file or in your narrative file):
# 1:
# 2:
# 3:

########################## (end of discussion problem 1)

#####################################################
# load the data into python (code provided for you) #
# (don't change any of this)                        #
#####################################################

import json

infile = open('horses_sample.json', 'r', encoding = 'utf-8')
data = json.load(infile)
infile.close()

#########################################################
# Code problem 1:  (no narrative expected for this one) #
# print the length and data type of the data variable   #
#########################################################



#############################################################
# Discussion problem 2 (4CR students only):                  #
# a) Explain why the length is 1000 (a few sentences)       #
# b) Explain why the data type says list and a bit about    #
#    the overall data structure of this data file.          #
#    (a few sentences)                                      #
# Please answer these in your narrative file, not in this   #
# script file.                                              #
#############################################################


############################################################################
# Coding problem 2: (narrative in narrative file, please)                  #
# Goal: count the number of horses born in each year, print the dictionary.#
# Info: Loop through the records, accessing the birth year.                #
#       Then use a dictionary counting pattern to count the years.         #
#       There are some horses without a birth years. For those records     #
#       missing that birthYear key (hint: check for membership),           #
#       set the value to be counted as 'missing' (string value.            #
############################################################################

# Sample results to check yours against:
# 25 horses were born in 1999.
# 35 horses are missing a birth year.
# 40 horses were born in 2003.



###########################################################################
# Coding problem 3: (narrative in narrative file, please)                 #
# Goal: write the counted birth years dictionary to a CSV file, and call  #
#       this file 'yearcounts.csv'                                        #
# Info: Follow the pattern showed in class.                               #
#       Create your outfile object, pass it to the csv.writer() fuction.  #
#       Write out the headers: year, count                                #
#       Loop through the counted dictionary via .items().                 #
#       Your rows will contain the birth year and the count.              #
#       Remember that you don't need to close the csvwriter object.       #
#       (Don't worry about sorting the years.)                            #
###########################################################################

# Example first 5 lines yearcounts.csv, as viewed from within pycharm
# (your first years might differ, but the format should be the same):
# year,count
# 1999,25
# 1986,18
# 1992,19
# missing,35



################################
# 2CR students are done!       #
# 4CR students continue below! #
################################



#######################################################################
# Coding problem 4: (narrative in narrative file, please)             #
# Goal: Write out the entire contents of the horses json              #
#       data file into a CSV, with missing values filled              #
#       in with 'missing' and the fields with wikidata ids            #
#       changed to from the URL to just the ID.                       #
#       Your headers should be:                                       #
#       horse, horseLabel, mother, father, birthyear, genderLabel     #
# Notes: You'll need to run horse, mother, father through the         #
#        get_id_from_url function to get just the ID out.             #
#        You'll need to run all values also through the clean_missing #
#        function in case there is a missing value.                   #
#        Use the same pattern as before to set this up.               #
#        Outfile, csv writer, write the headers. Then loop over the   #
#        data list, access what you need out of the records, clean it,#
#        then write the rows.                                         #
#######################################################################

