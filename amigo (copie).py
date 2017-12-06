import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

name_list = []
mail_list = []
smtp_list = []
final_dict = {}
id_list = []
i = 0
j = 0
k = 0
l = 0

#create wizard
#ask for date, number of participants and location

numb = input("Number of participants : ")
numb = int(float(numb))
date = input("date of the event : ")
location = input("location : ")

if numb % 2 == 0:
    while i < numb:
        name = str(input("Name of the participant : "))
        mail = str(input("mail of the participant : "))
        smtp = str(input("smtp of the participant : "))
        name_list.append(name)
        mail_list.append(mail)
        smtp_list.append(smtp)
        i += 1
        lim = (len(name_list)-1)
    while len(id_list) <= lim:
        id_numb = random.randint(0,lim)
        if id_numb not in id_list:
            if id_numb != i:
                id_list.append(id_numb)
                j += 1
    while k <= (len(name_list)-1):
       final_dict[name_list[k]] = name_list[id_list[k]]
       k += 1
       print('final_dict',final_dict) 
    ok = input("Do you agree with this repartition :y/n ")   
    if ok != 'y':
        print('run the program again')
    else:
        while l <= (len(name_list)-1):
            msg = MIMEMultipart()
            msg['From'] = 'xxx@gmail.com'
            msg['To'] = mail_list[l]
            msg['Subject'] = 'amigo invisible' 
            message = 'Hello {0} you are invited to take part to the amigo invisible on the {1} in {2} your friend is {3}'
            friend = final_dict.get(name_list[l])
            print(friend)
            message = message.format(name_list[l],date, location, friend)
            print(message)
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login('xxx@gmail.com', password)
            mailserver.sendmail('xxx@gmail.com',mail_list[l], msg.as_string())
            mailserver.sendmail(mail_list[l],'xxx@gmail.com', msg.as_string())
            mailserver.quit() 
            l += 1
else:
    print("you need an even number of participants")

