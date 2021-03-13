SAID JALAL SAIDI

HOW TO RUN:
IT REQUIRES PASSING A VALID URL AS COMMAND LINE ARGUMENT, FOR EXMAPLE:
pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-21_daily_incident_summary.pdf

HOW TO TEST:
IT REQUIRES TO USE "pipenv run pytest" AT THE ROOT LEVEL OF THE PROJECT

LIBRARIES, DEPENDENCIES, AND VIRTUAL ENVIRONMENT:
FIRST, A VIRTUAL ENVIRONMENT IS CREATED USING PYENV, WITH 3.8.6 PYTHON VERSION. 
SECOND, PROJECT0 MODULE IS INSTALLED IN THIS VIRTUAL ENV. 
THIRD, REQUIRED LIBRARIES TO RUN AND TEST IS MODULE ARE INSTALLED NAMELY "pipenv" and "pytest".
FOURTH, REQUIRED LIBRARIES FOR THE PROGRAM FUNCTIONALITIES ARE INSTALLED SUCH AS PYPDF2, WHICH IS NECESSARY FOR PDF READING.
FIFTH, OTHER LIBRARIES SUCH "urllib" FOR HTTP CONNECTION, "re" FOR REGEX SEARCH, "sqlite3" FOR SQL CONNECTION ARE IMPORTED.

ASSUMPTIONS:
THE MAIN PYTHON FILES ARE "main.py", WHICH INCLUDES THE MAIN FUNCTION. ALSO, "project0_main.py" WHICH INCLUDES IMPORTANT FUNCTIONALITIES SUCH AS DOWNLOADING THE INCIDENT RAW DATA, EXTRACTING THE INCIDENT OBJECTS, CREATE A SQLITE DATABASE AND TABLE, INSERTING INCIDENT OBJECTS INTO A TABLE, AND QUERIES THE INCIDENT NAUTRES WITH THEIR COUNTS.
ALSO, WE FOLLOWED THE OBJECT ORIENTED PROGRAMMING AND DEFINED "Incident"  CLASS IN "Incident.py", WHICH ENCAPSULATES SINGLE INCIDENT ROW IN PDF FILE. 
THE WORD SEPERATOR USED IN INCIDENT PDF FILES IS "\n". THE SAME CHARACTER IS USED TO SPLIT THE TEXT EXTRACTED FROM THE PDF FILE AND READ THE FILE ROW-WISE.
HOWEVER, THERE ARE SOME INCIDNTS WITH MULTIPLE LINE LOCATIONS. TO AVOID, READING A SINGLE LOCAION MORE THAN ONCE, TWO CONSECUTIVE INCIDENT NUMBERS ARE MARKED AND THEIR DISTANCE IS COMPUTED.
THE REASON IS THAT THIS ATTRIBUTE HAS A RELATIVELY ROBUST REGEX PATTERN. AFTER READING THE WHOLE DATA INTO A TEMPORARY PYTHON LIST, WE ADD SINGLE INCIDENT ROW TO A SMALL PYTHON LIST AND KEEP ADDING UNTIL WE HEAT THE NEXT INCIDENT NUMBER.
WE APPLY "\d{4}-\d{8}" REGEX MATCH. IF THE LENGTH OF THE SMALL LIST IS 7, THEN THE INCIDENT LOCATION IS SINGLE LINE. OTHERWISE, IT IS MULTI-LINE, WHICH TRIGGERS A FUNCTION TO LOCATE EACH LINE OF THE INCIDENT LOCATION AND MERGE THEM.
EACH EXTRACTED ROW, IS USED TO INSTANTIATE AN INSTANCE OF THE "Incident" class defined in "Incident.py". Each instance is added to a Python list, which will be finally i 
 

