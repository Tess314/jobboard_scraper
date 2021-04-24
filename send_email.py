import smtplib, ssl

def send_email(message):
    port = 465 #for SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "techietessie@gmail.com"
    receiver_email = "tesswattelders@gmail.com"
    password = "svvgoqbupnncfulb"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print("This was an automatic email.")
        except:
            print("Could not login or send the email.")
