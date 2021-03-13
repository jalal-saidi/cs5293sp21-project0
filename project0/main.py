import argparse
import project0_main
# requires a valid URL
def run(url):
    
    # fetches raw data from the remote url 
    incident_raw_data = project0_main.fetch_incidents(url)
    # create a list containing Incident objects
    incident_objects = project0_main.extract_incidents(incident_raw_data)
    try:
       # establish a connection to norman.db
       conn,cursor = project0_main.create_db()
       # fill norman.db with incident objects
       project0_main.populate_db(cursor, incident_objects)
       # Print the incident nature along with their counts
       project0_main.status(cursor)
    finally:
       # Close both database and cursor connection
       cursor.close()
       conn.close()
# Main function expects an --incidents command line argument       
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
    args = parser.parse_args()
    if args.incidents:
        run(args.incidents)
