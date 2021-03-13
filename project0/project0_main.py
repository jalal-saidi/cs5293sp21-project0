# HTTP connection
from urllib import request
# File I/O
import tempfile
# PDF reading
import PyPDF2
# Regex search and match
import re
# Sqlite
import sqlite3
# Incident class
from project0 import Incident
from project0.Incident import get_instance
# Downloads the raw data and writes it to a temprory file
# Requires a valid URL
def fetch_incidents(url):
   headers = {}
   headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
   data = request.urlopen(request.Request(url, headers=headers))
   fp = tempfile.TemporaryFile()
   # Write the pdf data to a temp file
   fp.write(data.read())
   # Set the curser of the file back to the begining
   fp.seek(0)
   # Read the PDF   
   return fp
# Creates a Python list of Incident objects
# Requires a temproray file holding raw incident data 
def extract_incidents(temp_file):
    # PDFreader handle
    pdfReader = PyPDF2.pdf.PdfFileReader(temp_file)
    # Holds all words in the PDF file
    temp_array=[]
    # Visit every single page in the PDF file
    for page in range(pdfReader.getNumPages()):
        # current PDF page
        current_page = pdfReader.getPage(page)
        # a string object containing all characters within a single page
        extracted = current_page.extractText()
        # Splits the string object using '\n' separator
        extracted_array=extracted.split('\n')
        # Append every single word to the temporary array
        for element in extracted_array:
                temp_array.append(element)
    
    # Defined an empty Python list for objects of the Incident class
    incidents = []
    # total dertermines the length a single row read from the temporary list
    # After each reading, a single row contains all elements from the current incident and 2 elements from the next row
    total = 0
    # is_first_group determines whether the first row from PDF file is visited
    is_first_group = True
    # Visits all elements in the temproary array except for the first 5 (header) and last 2 (elements)
    for data in temp_array[5:-2]:
      # Excludes empty entries and title of the PDF document
      if data!='' and  data !='NORMAN POLICE DEPARTMENT' and data !='Daily Incident Summary (Public)':
        # When total is 0, a new incident row is visited
        if total == 0:
            contains_incident_no = False
            # First row is visited
            if is_first_group:
                is_first_group= False
                group =[]
            # If it is not the first row then copy the date time and incident number from previous incident row to the current incident row
            else:
                temp_group = []
                temp_group.append(group[-2])
                temp_group.append(group[-1])
                contains_incident_no = True
                group = []
                group.append(temp_group[0])
                group.append(temp_group[1])
                total = 2
        group.append(data)
        total = total+1
        # Using the regex '\d{4}-\d{8}' to locate incident numbers
        match = re.search(r'\d{4}-\d{8}',data)
        if match:
            if contains_incident_no:
                # If the total number of elements is 7 then there is incident address is single line
                if total==7:
                   # instantiate an Incident object and append it to the list
                   instance = get_instance(group[0:-2])
                   incidents.append(instance)
                # If the total number of elements is more than 7 then there is incident address is multiple lines
                elif total > 7:
                   new_group=[]
                   extra = total-7
                   # Define an empty incident address
                   address = ''
                   # Convert the multiline address to a single address and append it a temproary list
                   for index,item in enumerate(group[0:-2]):
                      if index < 2 or index > 2 + extra:
                         new_group.append(item)
                      else:
                          address = address+' '+item
                          if index == 2+extra:
                            # remove the trailing spaces from the incident address
                            new_group.append(address.strip())

                   # instantiate an Incident object and append it to the list
                   instance = Incident.get_instance(new_group)
                   incidents.append(instance) 
                total=0
            else:
                contains_incident_no = True
    return incidents

# Establishes a connection to norman.db database
# Requires no parameters
def create_db():
    conn = sqlite3.connect('normanpd.db', isolation_level=None);
    cursor = conn.cursor()
    create_table_query = """CREATE TABLE IF NOT EXISTS incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
     nature TEXT,
    incident_ori TEXT)"""
    truncate_query= """DELETE FROM incidents"""
    # Create incidents table 
    cursor.execute(create_table_query)
    # Truncates incidents table before inserting new incident elements
    cursor.execute(truncate_query)
    return (conn,cursor)
# Inserts Incident objects into incidents table
# Requires an sqlite cursor and a list Incident objects
def populate_db(cursor, incident_values):
   insert_query = 'INSERT INTO incidents VALUES (?,?,?,?,?)'
   for value in incident_values:
       cursor.execute(insert_query, value.get_instance_to_array())
# Prints the incident nature with the count
def status(cursor):
    status_query = 'SELECT nature,COUNT(nature) FROM incidents GROUP BY nature ORDER BY nature'
    stat=cursor.execute(status_query).fetchall()
    print('Final Result:')
    for element in stat:
          print('{0}|{1}'.format(element[0],element[1]))
