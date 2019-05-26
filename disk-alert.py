import os
import smtplib
import subprocess

out = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE).communicate()[0]
print(out)

mail=smtplib.SMTP('smtp.gmail.com:587')
mail.ehlo()
mail.starttls()
mail.login('yesurkarvishal@gmail.com','nknkn19')
#mail.sendmail('*******@gmail.com','**********@gmail.com',content)
mail.close()