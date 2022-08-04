# firestore-to-notion

Note: This script only runs once, and once it has finished running, will stop.
I have setup a cron job on a web server that I host and added a Cron Job to run this script every 2 minutes.

Steps that this script takes:

1. Connects to our ChalkieApp FireStore Database using the serviceAcccountKey.json file
2. Reads the file into a dictionary for sorting
3. Dictionary is dumped into a json with keys to be able to access the json variables
4. the json variables are sorted, filtered, cleaned 
5. The new variables are piped into the Notion Database


If you find any issues/edge cases, please do let me know and I'll get to fixing them ASAP.


Data that is piped into Notion: Name, Profile Picture, University Email, Personal Email, Degree
