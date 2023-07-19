import smtplib
import datetime

def send_hi_email(receiver_email, sender_email, sender_password):
    # Set up the SMTP server for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    # Create a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    
    # Log in to your email account
    server.login(sender_email, sender_password)
    
    # Compose the email message
    subject = "Just saying hi!"
    message = f"Hi there,\n\nIt's been a while! Just wanted to drop a quick 'hi' and see how you're doing.\n\nBest regards,\n[Your Name]"
    msg = f"Subject: {subject}\n\n{message}"
    
    # Send the email
    server.sendmail(sender_email, receiver_email, msg)
    
    # Close the connection to the SMTP server
    server.quit()

# Replace the following variables with your own information
receiver_email = "recipient@example.com"  # Replace with the recipient's email address
sender_email = "your_email@example.com"   # Replace with your Gmail email address
sender_password = "your_email_password"   # Replace with your Gmail email password

# Check if a month has passed since the last interaction (you need to define this date)
last_interaction_date = datetime.date(2023, 6, 1)  # Replace with the last interaction date
current_date = datetime.date.today()

if (current_date - last_interaction_date).days >= 30:
    send_hi_email(receiver_email, sender_email, sender_password)

