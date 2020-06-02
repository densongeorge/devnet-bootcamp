#!/usr/local/bin/python3
from devnet_bootcamp import token

# Import Python requests library
import requests
from time import sleep

baseUrl = "https://api.ciscospark.com/v1"
headers = {"Authorization" : "Bearer " + token}


# Example 1 - Get group memberships

url = baseUrl + "/memberships"
r = requests.get(url, data={}, headers=headers)

if r.status_code == 200:
    print("GET membership response body - \n" + str(r.json()) + "\n")
    roomId = r.json()["items"][0]["roomId"]
else:
    print("Error while fetching membership "+str(r.status_code))
    print(r.json())
    exit()

# Example 2 - Get room details -

url = baseUrl + "/rooms/" + roomId
r = requests.get(url, data={}, headers=headers)

if r.status_code == 200:
    print("GET room details response body - \n" + str(r.json()) + "\n")
    print("Room title is " + r.json()["title"])
else:
    print("Error while fetching room details")
    print(r.json())
    exit()



# Example 3 - Get room members and store in a list -

url = baseUrl + "/memberships?roomId=" + roomId
r = requests.get(url, data={}, headers=headers)

if r.status_code == 200:
    #Store the roomId
    print("GET room memberships response body - \n" + str(r.json()) + "\n")
    member_list = []
    for member in r.json()["items"]:
        if member["personEmail"] in ["devnet-pune@webex.bot","rbhatawa@cisco.com"]:
            continue
        member_list.append(member["personEmail"])
    print(member_list)
else:
    print("Error while fetching room members list")
    print(r.json())
    exit()

# Example 4 - Post a message to the room

url = baseUrl + "/messages"
data = {
    "roomId" : roomId,
    "text" : "Guys, in the middle of the session. I will delete this message"
}
r = requests.post(url, data=data, headers=headers)

if r.status_code == 200:
    #Store the roomId
    print("Successfully posted a message in the room \n")
    messageId = r.json()["id"]
else:
    print("Error while posting the message")
    print(r.json())
    exit()

sleep(5)
# Example 5 - Delete the message you just posted.

url = baseUrl + "/messages/" + messageId

r = requests.delete(url, data={}, headers=headers)

if r.status_code == 204:
    #Store the roomId
    print("Successfully deleted the message in the room \n")
else:
    print("Error while deleting the message")
    print(r.json())
    exit()
