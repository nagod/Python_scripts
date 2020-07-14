
import smtplib, ssl, getpass

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = input("Enter your Email \n")
receiver_email = input("Who is receiving your Mail ? Enter his/her Mailadress \n")
password = getpass.getpass(prompt="Enter your Mail Password \n", stream=None)

# Create a secure SSL context
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()  # Can be omitted
    server.starttls(context=context)  # Secure the connection
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    print("Login was successful")
    msg = """\
    Subject: Hi there 
    
    This message is sent from Python."""

    server.sendmail(sender_email, receiver_email, msg)
    print("email has been send successfully")
except Exception as e:
    # Print any error messages to stdout
    print(e)
