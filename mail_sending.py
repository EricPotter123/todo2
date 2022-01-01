import smtplib


def run(email, body_par, subj):
    sender = "TheToDoAppTeam2021@outlook.com"
    receiver = email
    password = "12345!@#$%qwertQWERT"
    subject = subj
    body = body_par

    message = f'''From: {sender}\n
    To: {receiver}\n
    Subject: {subject} \n\n
    {body}
    '''

    server = smtplib.SMTP("smtp.outlook.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Email sent!")
        server.quit()

    except smtplib.SMTPAuthenticationError:
        print("Unable to sign in...")

run("puscasueric2011@gmail.com", "hi", "hello")
