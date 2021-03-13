# Each instance of Incident class represents single incident in the PDF file
class Incident:
    # The constructor requries date/time, incident number, location, nature as well as the ORI
    def __init__(self, date_time, incident_no, location, nautre,ori):
        self.date_time = date_time
        self.incident_no = incident_no
        self.location = location
        self.nautre= nautre
        self.ori = ori
    # Date-time getter 
    def get_data_time(self):
        return self.date_time

    # Incident Number getter
    def get_incident_no(self):
        return self.incident_no
    
    # Location getter
    def get_location(self):
        return self.location

    # Incident Nature Getter
    def get_nature(self):
        return self.nautre

    # ORI getter
    def get_ori(self):
        return self.ori

    # Represents an instance of Incident class using Python list
    def get_instance_to_array(self):
             incident_array = []
             incident_array.append(self.date_time)
             incident_array.append(self.incident_no)
             incident_array.append(self.location)
             incident_array.append(self.nautre)
             incident_array.append(self.ori)
             return incident_array

# Instantiate an Incident object from a Python list
def get_instance(incident_array):
       instance = Incident(incident_array[0], incident_array[1],incident_array[2],incident_array[3],incident_array[4])
       return instance
