from twilio.rest import Client


def send_message(account_sid, auth_token, from_, to, message_body='Hello' ):

    client = Client(account_sid, password=auth_token)

    message = client.messages.create(
        from_=from_,
        body=message_body,
        to=to
    )

    return message.sid
