import matchmake
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(giver_surname, giver_firstname, giver_email, reciever):
    me = "youremail@blah.com"
    my_password = "yourpassword"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Kris Cindle"
    msg['From'] = me
    msg['To'] = giver_email

    html = f"<html><body><p>Hey there {giver_firstname}. You've been matched with: {reciever[0]}</p></body></html>"
    part2 = MIMEText(html, 'html')

    msg.attach(part2)

    # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
    s = smtplib.SMTP_SSL('smtp.gmail.com')
    # do the smtp auth; sends ehlo if it hasn't been sent already
    s.login(me, my_password)

    s.sendmail(me, giver_email, msg.as_string())
    s.quit()

print(send_email("giver_surname", "giver_firstname", "giver_email", matchmake.make("giver_surname", "giver_firstname")))
