from twilio.rest import Client
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' 
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+15017122661',
    body ='body',
    to ='+15558675310'
)
print(message.sid)
