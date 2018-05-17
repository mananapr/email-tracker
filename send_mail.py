#############
## IMPORTS ##
#############
import time
import smtplib
from shutil import copyfile
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

## DECLARATIONS
## YOU - your email address
## PASS - password for your email id
## TARGET - target email address
## FILENAME - the address on your server where the gif is served
YOU = ""
PASS = ""
TARGET = ""
FILENAME = "http://mananapr.dynu.net:8000/gifs/" + TARGET + ".gif"

## Copying the base gif to the same directory with name as that of the target email address
copyfile("/var/www/html/gifs/collect.gif", "/var/www/html/gifs/"+TARGET+".gif")

## Connect to SMTP Server
server = smtplib.SMTP('', 587)
server.starttls()
server.login(YOU, PASS)

## Message
msg = MIMEMultipart('alternative')
msg['Subject'] = ""
msg['From'] = YOU
msg['To'] = TARGET
text = ""
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       <img src="{0}">
    </p>
  </body>
</html>
"""
## Embed the image link in file
html = html.format(FILENAME)

## Attach the html and text to the mail
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')
msg.attach(part1)
msg.attach(part2)

## Send the mail and disconnect from server
server.sendmail(YOU, TARGET, msg.as_string())
server.quit()
