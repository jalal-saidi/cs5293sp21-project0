from project0 import project0_main
from project0 import Incident
import pytest
import sqlite3
# Test wether the number of rows in the incident table is 0
def test_create_db():
 conn,cursor= project0_main.create_db()
 result = cursor.execute('SELECT * FROM incidents').fetchall()
 assert len(result)==0
test_create_db()
# Test the insert incident
# Successul test should at least insert one row into incident table
def test_populate_db():
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
  incidents = []
  group = ['2021-03-01', "some_id", "some_location","some_nature","some_ori"]
  inc1= Incident.get_instance(group)
  incidents.append(inc1)
  project0_main.populate_db(cursor,incidents)
  result = cursor.execute('SELECT * FROM incidents').fetchall()
  assert len(result)==1
test_populate_db()
