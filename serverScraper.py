#Scrapes -ServerName -TotalMembers -OnlineMembers -VanityCode
#API Endpoint :- https://discord.com/api/v9/invites/{inviteCode}?with_counts=true&with_expiration=true

import requests
import time

invites = open("invites.txt", 'r')

for invite in invites:
    invite = invite.rstrip()
    print("Working on invite: ", invite)
    url = "https://discord.com/api/v9/invites/{}?with_counts=true&with_expiration=true".format(invite)
    response = requests.get(url)
    info = response.json()
    
    with open("serverNames.txt", "a", encoding="utf-8") as names:
        names.write("{}\n".format(info["guild"]["name"]))
        names.close()

    with open("totalMembers.txt", "a") as tMembers:
        tMembers.write("{}\n".format(info["approximate_member_count"]))
        tMembers.close()

    with open("onlineMembers.txt", "a") as oMembers:
        oMembers.write("{}\n".format(info["approximate_presence_count"]))
        oMembers.close()

    with open("vanityCodes.txt", "a") as vanity:
        vanity.write("{}\n".format(info["guild"]["vanity_url_code"]))
        vanity.close()

    time.sleep(5)

print("--- --- Task Completed --- ---")
invites.close()
