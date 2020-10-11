from twilio.rest import Client
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #Enter your Account SID here 
auth_token = 'your_auth_token' #Enter Token here
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+15017122661',  #Enter trial number
    body ='body', #Enter message here
    to ='+15558675310' #Enter verifred number with your twilio account
)
print(message.sid)
