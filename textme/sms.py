import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC4bd0ef5a7a777b65e0a698a8c4663865']
auth_token = os.environ['52c192d46b062abde74f2da2719e632c']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there! i am your sms bot !',
                              from_='+17073294447',
                              to='+918898779021'
                          )

print(message.sid)