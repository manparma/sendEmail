import smtplib, ssl
import config
import datetime as dt
import time
# import schedule


def send_email(subject, msg):
    # try:
    #     schedule.every(10).seconds.do(send_email(subject,msg))
    #     schedule.every().saturday.at('12:00').do(send_email(subject,msg())
    # while 1:
    #     schedule.run_pending()
    #     time.sleep(1)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.LOGIN_ADDRESS, config.PASWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("e-mail sent!")
    # except:
    #     print("Failed to send e-mail")


send_time = dt.datetime(2021,3,20,9,12,57) # set your sending time in UTC
time.sleep(send_time.timestamp() - time.time())

subject = 'This is a test subject'
msg = 'This is a test message'

send_email(subject, msg)
