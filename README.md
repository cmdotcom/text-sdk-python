# text-sdk-python

## A helper library to sending messages using python.
Want to send messages in your Python application? Then you are at the right address.
If you want to get all the functionalities, go to: [CM.com API Docs](https://docs.cmtelecom.com/bulk-sms/v1.0)

## Installing
Under Construction

## Instantiate the client
Use your productToken which authorizes you on the CM platform. Get yours on CM.com

```cs
from CMText.TextClient import TextClient

client = TextClient(apikey=key)
```

## Send a message
By calling `SendSingleMessage` and providing message text, sender name, recipient phone number(s).

```cs
   client = TextClient(apikey=key)
   client.SendSingleMessage(message=message, from_='CM.com', to=Recipients)
```

## Sending multiple messages
By calling `AddMessage` and providing message text, sender name, recipient phone number(s) you can queue multiple messages. Send them by calling `send`.

```cs
   client = TextClient(apikey=key)
   client.AddMessage(message=message, from_='pythonSDK', to=Recipients)
    client.AddMessage(message=message2, from_='pythonSDK', to=Recipients2)
   response = client.send()
```

## Sending a rich message
Under construction

## Get the result
Sending a message by calling `send` returns the response body. Response is of type: https://requests.readthedocs.io/en/master/user/quickstart/#response-content
```cs
   response = client.send()
```