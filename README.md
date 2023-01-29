Said Jalal Saidi

How to run:
It requires passing a valid URL as a command line argument, for example:
Pipenv run python project0/main.Py --incidents https://www.normanok.gov/sites/default/files/documents/2021-02/2021-02-21_daily_incident_summary.pdf

How to test:
It requires to use "Pipenv run pytest" at the root level of the project

Libraries, dependencies, and virtual environment:
First, a virtual environment is created using pyenv, with 3.8.6 python version. 
Second, the project0 module is installed in this virtual env. 
Third, required libraries to run and the test is module is installed namely "Pipenv" and "Pytest".
Fourth, required libraries for the program functionalities are installed such as pypdf2, which is necessary for pdf reading.
Fifth, other libraries such "Urllib" for HTTP connection, "Re" for regex search, and "Sqlite3" for SQL connection are imported.

Assumptions:
The main python files are "Main.Py", which includes the main function. Also, "Project0_main.Py" which includes important functionalities such as downloading the incident raw data, extracting the incident objects, creating a SQLite database and table, inserting incident objects into a table, and querying the incident natures with their counts.
Also, we followed the object-oriented programming and defined "Incident"  class in "Incident.Py", which encapsulates a single incident row in a pdf file. 
The word separator used in incident pdf files is "\n". The same character is used to split the text extracted from the pdf file and read the file row-wise.
However, there are some incidents with multiple line locations. To avoid, reading a single location more than once, two consecutive incident numbers are marked and their distance is computed.
The reason is that this attribute has a relatively robust regex pattern. After reading the whole data into a temporary python list, we add a single incident row to a small python list and keep adding until we heat the next incident number.
We apply "\d{4}-\d{8}" regex match. If the length of the small list is 7, then the incident location is a single line. Otherwise, it is multi-line, which triggers a function to locate each line of the incident location and merge them.
Each extracted row is used to instantiate an instance of the "Incident" class. Each instance is added to a python list and is used to insert a single incident record into "Incidents" sqlite3 table. Finally, the "Status" function retrieves the incident natures along with their counts.

Test cases:
Test cases are included in "Project0_test.Py". Two test cases are written; first,"Test_create_db" for testing the successful database creation and table creation. This test case examines if the number of rows in "Incidents" table is 0.
The second test case is test_populate_db. This function checks if a single object of "Incident" class can be inserted successfully. 
