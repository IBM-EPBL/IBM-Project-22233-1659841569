import os
from dotenv import load_dotenv

load_dotenv()
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def sendmail(usermail,subject,content):
    message = Mail(from_email='410619104029@smartinternz.com',to_emails=usermail,subject=subject,html_content='<strong> {} </strong>'.format(content))
    try:
        sg = SendGridAPIClient(os.getenv('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'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
