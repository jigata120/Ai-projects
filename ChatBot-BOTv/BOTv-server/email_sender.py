import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email, subject, message):
     
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'chatbotbotv@gmail.com'   
    sender_password = 'example_pass'  

  
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
 
    msg.attach(MIMEText(message, 'plain'))

    try:
 
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  
        server.login(sender_email, sender_password)

 
        server.send_message(msg)
        server.quit()

        return f'Email sent to {recipient_email}'
    except Exception as e:
       return f'Failed to send email. Error: {str(e)}'


if __name__ == "__main__":
    send_email('pplesho@gmail.com', 'Explore Your Chat Conversation ID', f'Here is your chat conversation ID: {""}')
