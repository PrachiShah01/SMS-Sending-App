from twilio.rest import Client
account_sid = 'AC313d895ac98f51cf6ad24b2bf6a5bf68'
auth_token = '8d40f7aad32ccef658ff1beed7cdd3d5'
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+12015834824',
    body ='Hello!!! Prachi here',
    to ='+918758675093'
)
print(message.sid)