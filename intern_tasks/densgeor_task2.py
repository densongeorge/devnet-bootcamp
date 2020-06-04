import requests
from token1 import *

room_name = "FY20 - Internship DevNet Training Program & Workshop | June 1-4 | Batch 10"
rooms_endpoint = "https://webexapis.com/v1/rooms"


headers = {"Authorization": "Bearer "+token }

r = requests.get(rooms_endpoint,headers=headers)

k = r.json()

all_rooms = k['items']
required_id = ""
for room in all_rooms :
    if room["title"]== room_name :
        required_id = room["id"]

room_membership_endpoint = "https://webexapis.com/v1/memberships?roomId="+required_id

r = requests.get(room_membership_endpoint,headers=headers)

k = r.json()

org_stats_endpoint = "https://orgstats.cisco.com/api/1/entries?users="

all_members = k['items']
print(len(all_members))
cisco_employees = []
cecids = []
cisco_employees_with_org = []


for member in all_members:
    final_employee_dict ={}
    if "@cisco.com" in member['personEmail'] :
        cisco_employees.append(member)
        cecids.append(member['personEmail'] [:-10])
        print("Fetching employee cecid and employee name")
        final_employee_dict["Employee Display Name"]= member["personDisplayName"]
        cecid = member['personEmail'] [:-10]
        final_employee_dict["cecid"]=cecid
        r = requests.get(org_stats_endpoint+cecid)
        k = (r.json())[0]
        final_employee_dict["Director CECID"] = k['d']
        final_employee_dict["Manager CECID"]= k['m']
        print("Fetching manager name and director name of the employee")
        r = requests.get(org_stats_endpoint+final_employee_dict["Director CECID"])
        k = (r.json())[0]
        final_employee_dict["Director Name"]= k["N"]
        r = requests.get(org_stats_endpoint+final_employee_dict["Manager CECID"])
        k = (r.json())[0]
        final_employee_dict["Manager Name"]= k["N"]
        cisco_employees_with_org.append(final_employee_dict)
        #print(final_employee_dict)
        
#print(len(cisco_employees_with_org))
# sample output = 
# {'Director Name': u'Kiran Deshpande', 'Manager Name': u'Kiran Deshpande', 'Manager CECID': u'kirdeshp', 'cecid': u'densgeor', 'Director CECID': u'kirdeshp', 'Employee Display Name': u'Denson George'}
# {'Director Name': u'Shajith Moosa', 'Manager Name': u'Amitashwa Agarwal', 'Manager CECID': u'amitaaga', 'cecid': u'mpapiset', 'Director CECID': u'smoosa', 'Employee Display Name': u'Manoj Papisetty'}
