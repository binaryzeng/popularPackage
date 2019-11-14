from twilio.rest import Client

acc_id="AC9fd981eb206dfa9c223d1343e504ddc0"
acc_token="fafc426273f43178e34807e62b64ebe3"

client = Client(acc_id, acc_token)
call = client.messages.create(
    to="15149999999",
    from_="14389999999",
    body="This is a test message sent by Pysms"
)
call.date_sent
