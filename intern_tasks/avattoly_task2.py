# Nothin here
#TASK 2
import requests
import json
url_listgroups="https://webexapis.com/v1/rooms"

token="MWEwOGQ1MzYtZTFlNS00YmRjLTg2ZDgtOTAzZDRmZTViNTZhMzQ0ZjI4MTktNzMy_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
headers={"Authorization":"Bearer {}".format(token)}
#  1)
data =requests.get( url_listgroups, headers=headers)
for item in data.json()["items"]:
    if "Internship DevNet Training Program & Workshop | June 1-4 | Batch 10" in item['title']:
        group_id=item['id']
        break
membership = "https://webexapis.com/v1/memberships"
membership+=("?roomId={}".format(group_id))
# print(membership)

groupMembers=requests.get(membership,headers=headers).json()["items"]
# print(groupMembers)
#2)
ciscoMembers=[]
for members in groupMembers:
    if "@cisco.com" in members['personEmail']:
        ciscoMembers.append(members)
#3)
personalDetailurl="https://orgstats.cisco.com/api/1/entries?users="
for members in ciscoMembers:
    personalDetailurl+=(members["personEmail"][0:members["personEmail"].index("@")] + ",")
memberDetails=requests.get(personalDetailurl).json()

#4)
finalData=[]
for member in memberDetails:
    data={}
    data['cec']=member['I']
    data['manager']=member["m"]
    finalData.append(data)
print(finalData)


