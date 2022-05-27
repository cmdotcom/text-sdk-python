import os
from CMText.TextClient import TextClient
from CMText.whatsapp_interactive.MessageBuilder import MessageBuilder

# fetch the API key from environment variables
UNIQUE_API_KEY = os.getenv("CM_API_KEY")
if UNIQUE_API_KEY is None:
    print('Please fill an environment variable named CM_API_KEY with your API key.')

to = ['your-phone-number']

# Instantiate client with your own api-key
client = TextClient(apikey=UNIQUE_API_KEY)

mb_header = MessageBuilder.create_interactive_message_header(type='text', text='my-header', media=None)
mb_body = MessageBuilder.create_interactive_message_body(text='my-body-text')
mb_footer = MessageBuilder.create_interactive_message_footer(text='my-footer-text')

# Create rows for when the user clicks on the button
mb_rows = [MessageBuilder.create_interactive_message_action_row(title='row1-content',
                                                                id='sect1-id1',
                                                                description='row1-description'),
           MessageBuilder.create_interactive_message_action_row(title='row2-content',
                                                                id='sect1-id2',
                                                                description='row2-description')]

mb_rows2 = [MessageBuilder.create_interactive_message_action_row(title='row1-content',
                                                                 id='sect2-id1',
                                                                 description='row1-description'),
            MessageBuilder.create_interactive_message_action_row(title='row2-content',
                                                                 id='sect2-id2',
                                                                 description='row2-description')]

# Divide the rows into different sections
section1 = MessageBuilder.create_interactive_message_action_section(title='section1', rows=mb_rows)
section2 = MessageBuilder.create_interactive_message_action_section(title='section2', rows=mb_rows2)

mb_section = [section1, section2]

mb_action = MessageBuilder.create_interactive_message_action(button='cta-button-content', buttons=[],
                                                             sections=mb_section)

mb_interactive = MessageBuilder.create_interactive_message(type='list', header=mb_header, body=mb_body,
                                                           footer=mb_footer, action=mb_action)

client.add_whatsapp_interactive_message(from_="pythonSDK", interactive=mb_interactive, to=to)

# Instantiate client with your own api-key
response = client.send()

# Response is an object of type: https://www.w3schools.com/python/ref_requests_response.asp
print(response.text)
