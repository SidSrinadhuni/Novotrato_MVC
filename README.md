# Novotrato_MVC

# Overview
This repository contains two Python scripts that are designed to automate the process of downloading a PDF from the Boletin website and subsequently emailing it to a list of recipients. These scripts are scheduled to run daily at 8 AM through a cron job.

# Scripts
download_pdf.py: This script is responsible for downloading the latest PDF from the Boletin website. It checks for new publications and downloads the most recent one, storing it locally.

send_email.py: After the successful download of the PDF, this script is triggered. It sends the downloaded PDF as an email attachment to a predefined list of recipients.

# Automation
The scripts are executed daily at 8 AM through a cron job, ensuring that the process is fully automated and requires no manual intervention.

# Email Sending Mechanism
To send emails, we utilize the SendGrid API. Due to security reasons, we do not store credentials directly in the system or the code.
Instead, we use a SendGrid API key. This key is hardcoded in the send_email.py script.
The API key authenticates our credentials with SendGrid and generates an API token, which is then used to send the emails.

# SendGrid API Key
Important: The API key is a sensitive piece of information. It should be handled with utmost care and should not be shared publicly.
The current implementation has the API key hardcoded, which is not a recommended practice for production environments. Consider using environment variables or a secure key management system in a production setting.
# Email Recipients
The list of email recipients is defined within the send_email.py script.
This list can be modified as per requirements. Ensure that the email addresses are valid and authorized to receive these communications.
# Dependencies
Both scripts require certain Python libraries. Ensure that these dependencies are installed and up-to-date.
For sending emails, the send_email.py script requires the SendGrid Python library. This can be installed via pip:
Copy code
pip install sendgrid

# Usage
To use these scripts, clone this repository to your local system or server where the cron job is set up.
Ensure that Python is installed and the required libraries are available.

# Security and Best Practices
Regularly update the API key and monitor its usage.
Consider implementing additional security measures like API key rotation and usage alerts.
Avoid hardcoding sensitive information in the scripts. Explore secure ways to store and access such data.

# Contribution
Contributions to improve the scripts or the overall workflow are welcome. Please follow the standard procedure for contributions to this repository.
