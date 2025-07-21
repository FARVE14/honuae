"""

This module can be used to send the mail.

"""

__author__ = "Faisal Ahmed"

import os
from dotenv import load_dotenv
import smtplib
import ssl
from email.message import EmailMessage


load_dotenv()

def send_email_with_attachment(
        time_dict: dict, host_url: str, no_of_attempts: int,
        file_path: str | bool = False) -> bool | ValueError:
    """
    Send email with attachment
    :param time_dict:
    :param host_url:
    :param no_of_attempts:
    :param file_path:
    :return:
    """

    sender = os.getenv('SENDER_EMAIL')
    recipient = os.getenv('RECIPIENT_EMAIL')
    app_password = os.getenv('APP_PASSWORD')
    git_repo_link = os.getenv('GIT_REPO_LINK')

    if sender is None or recipient is None or app_password is None:
        return ValueError("sender | recipient | app_password not set")

    subject = f"[Automated Generated Mail] Website Load Time Report for {host_url}"
    body = f"""
    Hi All, 
    This is an automatically generated report from GitHub Actions.
    Website tested: {host_url}
    Number of attempts: {no_of_attempts}

    📊 Load Time Summary:
    - Mean Time: {time_dict.get("mean_time", 0):.2f} seconds
    - Max Time: {time_dict.get("max_time", 0):.2f} seconds
    - Min Time: {time_dict.get("min_time", 0):.2f} seconds

    Please find the attached graph for detailed performance metrics.
    
    Regards,  
    Faisal
    
    ---
    📌 *Note:*  
    This report has been generated using **GitHub Actions CI/CD pipeline**.  
    You can view or contribute to the code at:  
    🔗  Repo: {git_repo_link}
    --- 
"""

    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    if file_path:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            file_name = file.name
            msg.add_attachment(file_data, maintype='image', subtype='png', filename=file_name)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)
        print("✅ Email sent successfully.")

    return True
