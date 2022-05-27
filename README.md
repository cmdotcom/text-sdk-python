# Text-sdk-python
![publish to PyPi](https://github.com/cmdotcom/text-sdk-python/workflows/publish%20to%20PyPi/badge.svg)
![PyPi](https://img.shields.io/pypi/v/CM_text_sdk_python
)

## A helper library to sending messages using python.
Want to send messages in your Python application? Then you are at the right address.
If you want to get all the functionalities, go to: [CM.com API Docs](https://docs.cmtelecom.com/bulk-sms/v1.0)

## Installing
Include the SDK by downloading the files manually or running the following command in a Python Shell.
```cs
    pip install CM_Text_sdk_python
```

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
By calling `AddRichMessage` and providing `Media`, message text, sender name, recipient phone number(s) you can queue multiple Rich messages. Send them by calling `send`.

```cs
    media = {
            "mediaName": "conversational-commerce",
            "mediaUri": "https://www.cm.com/cdn/cm/cm.png",
            "mimeType": "image/png"
        }

    client = TextClient(apikey=key)
    client.AddRichMessage(message=message, from_='pythonSDK', to=to, allowedChannels=allowedChannels, media=media)
    response = client.send()
```

## Sending a Whatsapp Template message
By calling `AddWhatsappTemplateMessage` and providing `Template`, sender name, recipient phone number(s) you can queue multiple Whatsapp Template messages. Send them by calling `send`.

```cs
    template_namespace = "Your-Template-Namespace"
    template_element_name = "Replace with Template Name"
    template = WhatsappTemplate(template_namespace, template_element_name)
    
    client = TextClient(apikey=key)
    client.AddWhatsappTemplateMessage(from_='pythonSDK', to=to, template=template)
    response = client.send()
```

See Examples folder for more examples.

## Sending Interactive Whatsapp message
See the examples folder for an example.

## Get the result
Sending a message by calling `send` returns the response body. Response is of type: https://requests.readthedocs.io/en/master/user/quickstart/#response-content
```cs
    response = client.send()
```