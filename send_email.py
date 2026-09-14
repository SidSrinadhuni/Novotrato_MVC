import os
import datetime
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

def send_email_with_pdf(api_key, sender_email, recipient_email, subject, content, pdf_file_path):
    # Create a Mail object
    message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject=subject,
        plain_text_content=content
    )

    # Read PDF file as binary
    with open(pdf_file_path, 'rb') as f:
        data = f.read()
        f.close()

    # Encode the binary data to base64
    encoded = base64.b64encode(data).decode()

    # Create an Attachment object
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/pdf')
    attachment.file_name = FileName(os.path.basename(pdf_file_path))
    attachment.disposition = Disposition('attachment')

    # Add attachment to the message
    message.attachment = attachment

    # Send the email
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(f"Email sent! Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
current_date = datetime.datetime.now().strftime("%m-%d-%Y")
api_key = ''  # Replace with your API key
sender = 'hitmeonthisaddress@gmail.com'  # Replace with your email
recipient = ['hitmeonthisaddress@gmail.com','noel@novotrato.com']  # Replace with recipient's email
subject = f"Labor Boletin for {current_date}"
content = f"""
Hola,

I hope this email finds you well. We are pleased to send you labor bulletin, dated {current_date}, as an attachment to this email. This bulletin is a key source of latest information and updates from the Boletín Laboral Mayo.

Should you have any questions or need further information, feel free to reach out to us.
Have a nice day!

Best regards,
Sid
"""
pdf_name = f"Boletin Laboral CDMX {current_date}.pdf"
pdf_path = os.path.join('/home/ec2-user/',pdf_name)  # Replace with the path to your PDF file

send_email_with_pdf(api_key, sender, recipient, subject, content, pdf_path)
