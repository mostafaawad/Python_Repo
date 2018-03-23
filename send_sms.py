# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC3db3f1600a4d7e9e2db9edab90a53262"
auth_token = "dc90181242c4b494a7a6268b022deb97"

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+201114548637",
    from_="+12018700982",
    body="Hello there!")
print message.sid