import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import datetime
from tqdm import tqdm
from time import sleep
import random

Chelovek = input("Напишите кого сносим [Пример: @durov] >")
def sendemail(senderemail, senderpassword, recipientemail, subject, messagetext):
    try:
        if '@yahoo.com' in senderemail:
            smtp = 'smtp.mail.yahoo.com'
        elif '@mail.ru' in senderemail:
            smtp = 'smtp.mail.ru'
        elif '@bk.ru' in senderemail:
            smtp = 'smtp.mail.ru'
        elif '@inbox.ru' in senderemail:
            smtp = 'smtp.mail.ru'
        elif '@list.ru' in senderemail:
            smtp = 'smtp.mail.ru'
        elif '@internet.ru' in senderemail:
            smtp = 'smtp.mail.ru'
        elif '@payeerbox.ru' in senderemail:
            smtp = 'smtp.mail.ru'
        elif '@gmail.com' in senderemail:
            smtp = 'smtp.google.com'
        elif '@outlook.com' in senderemail:
            smtp = 'smtp-mail.outlook.com'
        elif '@hotmail.com' in senderemail:
            smtp = 'smtp-mail.outlook.com'
        else:
            smtp = 'smtp.rambler.ru'
            smtp = 'smtp.google.com'
        server = smtplib.SMTP(smtp, 587) # SMTP адресс вашего почтового провайдера. к примеру smtp.mail.ru или smtp.google.com и т.д.
        server.starttls()
        server.login(senderemail, senderpassword)

        message = MIMEMultipart()
        
        message['From'] = senderemail
        message['To'] = recipientemail
        message['Subject'] = subject

        body = messagetext
        message.attach(MIMEText(body, 'plain'))

        server.send_message(message)
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"))
        print(f"Письмо от {senderemail} успешно отправлено на {recipientemail}.")


        server.quit()
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")

def read_accounts_from_file(filename):
    accounts = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                accounts.append((parts[0], parts[1]))
    return accounts


# Чтение аккаунтов из файла
account_file = "senders.txt"
senders = read_accounts_from_file(account_file)

recipients = [
    "surpe52@gmail.com",
    "support@telegram.org",
    "dmca@telegram.org",
    "abuse@telegram.org"

]

messages = [
f"Уважаемая поддержка Telegram, прошу обратить внимание на аккаунт {Chelovek}, который активно торгует наркотическими веществами. Прошу принять меры по блокировке данного аккаунта.",
f"Здравствуйте, хочу сообщить о том, что аккаунт {Chelovek} занимается мошенничеством, предлагая ложные товары и услуги. Прошу принять соответствующие меры.",
f"Добрый день, обращаю ваше внимание на аккаунт {Chelovek}, который осуществляет слив личных данных пользователей без их согласия. Просьба принять меры по блокировке данного аккаунта.",
f"Здравствуйте, прошу проверить аккаунт {Chelovek} на наличие контента, связанного с распространением наркотических веществ. Такие действия недопустимы и требуют немедленного вмешательства.",
f"Уважаемая поддержка Telegram, обращаю ваше внимание на аккаунт {Chelovek}, который занимается мошеннической деятельностью, обещая выгодные предложения и не выполняя их. Просьба принять меры.",
f"Добрый день, хотел бы сообщить о том, что аккаунт {Chelovek} размещает информацию, способствующую распространению наркотических веществ. Прошу принять необходимые действия.",
f"Здравствуйте, прошу провести проверку аккаунта {Chelovek} на предмет нарушения правил использования платформы в связи с мошеннической деятельностью. Просьба принять меры.",
f"Уважаемая поддержка Telegram, обращаю ваше внимание на аккаунт {Chelovek}, который публикует личные данные пользователей без их согласия. Просьба принять меры по блокировке данного аккаунта.",
f"Добрый день, хочу сообщить о том, что аккаунт {Chelovek} продает поддельные товары и обманывает своих клиентов. Прошу принять соответствующие меры.",
f"Здравствуйте, прошу обратить внимание на аккаунт {Chelovek}, который распространяет информацию о наркотических веществах и может нанести ущерб сообществу. Просьба принять необходимые меры.",
f"Уважаемая поддержка Telegram, прошу обратить внимание на аккаунт {Chelovek}, который активно пропагандирует насилие и экстремистские идеи. Прошу принять меры по блокировке данного аккаунта.",
f"Здравствуйте, хочу сообщить о том, что аккаунт {Chelovek} размещает порнографический контент и нарушает правила использования платформы. Прошу принять соответствующие меры.",
f"Добрый день, обращаю ваше внимание на аккаунт {Chelovek}, который распространяет дезинформацию и фейковые новости. Просьба принять меры по блокировке данного аккаунта.",
f"Здравствуйте, прошу проверить аккаунт {Chelovek} на предмет нарушения авторских прав и пиратства. Такие действия недопустимы и требуют немедленного вмешательства.",
f"Уважаемая поддержка Telegram, обращаю ваше внимание на аккаунт {Chelovek}, который проводит финансовые мошенничества и обманывает пользователей. Просьба принять меры.",
f"Добрый день, хотел бы сообщить о том, что аккаунт {Chelovek} нарушает законы о защите личных данных и использует их без согласия пользователей. Прошу принять необходимые действия.",
f"Здравствуйте, прошу провести проверку аккаунта {Chelovek} на предмет незаконной торговли оружием или другими запрещенными товарами. Просьба принять меры.",
f"Уважаемая поддержка Telegram, обращаю ваше внимание на аккаунт {Chelovek}, который проводит кибербуллинг и угрожает другим пользователям. Просьба принять меры по блокировке данного аккаунта.",
f"Добрый день, хочу сообщить о том, что аккаунт {Chelovek} создает фейковые конкурсы и лотереи, обманывая пользователей. Прошу принять соответствующие меры.",
f"Здравствуйте, прошу обратить внимание на аккаунт {Chelovek}, который распространяет информацию о самоповреждающем поведении и может навредить здоровью пользователей. Просьба принять необходимые меры.",
f"Dear Telegram support, please pay attention to the account {Chelovek}, which actively trades in narcotic substances. Please take measures to block this account.",
f"Hello, I would like to report that the account {Chelovek} is engaged in fraud, offering false goods and services. Please take appropriate action.",
f"Good afternoon, I draw your attention to the account {Chelovek}, which is leaking users' personal data without their consent. Please take measures to block this account.",
f"Hello, please check the {Chelovek} account for content related to the distribution of narcotic substances. Such actions are unacceptable and require immediate intervention.",
f"Dear Telegram support, I draw your attention to the account {Chelovek}, which is engaged in fraudulent activities, promising lucrative offers and failing to fulfill them. Please take action.",
f"Good afternoon, I would like to inform you that the {Chelovek} account is posting information that promotes the distribution of narcotic substances. Please take the necessary action.",
f"Hello, I would like to request a review of the {Chelovek} account for violating the platform's terms of use due to fraudulent activity. Please take action.",
f"Dear Telegram support, I draw your attention to the account {Chelovek}, which publishes personal data of users without their consent. Please take measures to block this account.",
f"Good afternoon, I would like to inform you that the account {Chelovek} is selling fake goods and cheating its customers. Please take appropriate action.",
f"Hello, please pay attention to the account {Chelovek}, which is spreading information about narcotic substances and may cause damage to the community. Please take the necessary measures.",
f"Dear Telegram support, please pay attention to the account {Chelovek}, which actively promotes violence and extremist ideas. Please take measures to block this account.",
f"Hello, I would like to report that the {Chelovek} account is posting pornographic content and violating the platform's terms of use. Please take appropriate action.",
f"Good afternoon, I draw your attention to the account {Chelovek}, which spreads misinformation and fake news. Please take measures to block this account.",
f"Hello, please check the {Chelovek} account for copyright infringement and piracy. Such actions are unacceptable and require immediate intervention.",
f"Dear Telegram support, I draw your attention to the account {Chelovek}, which conducts financial fraud and deceives users. Please take action.",
f"Good afternoon, I would like to inform you that the {Chelovek} account is violating privacy laws and using personal data without users' consent. Please take the necessary action.",
f"Hello, I would like to request a background check on the {Chelovek} account for illegal trading of weapons or other prohibited goods. Please take action.",
f"Dear Telegram support, I draw your attention to the account {Chelovek}, which conducts cyberbullying and threatens other users. Please take steps to block this account.",
f"Good afternoon, I would like to report that the account {Chelovek} creates fake contests and lotteries, cheating users. Please take appropriate action.",
f"Hello, please pay attention to the account {Chelovek}, which spreads information about self-harming behavior and can harm the health of users. Please take the necessary measures."
]

subjects = [ # можешь написать и больше тем по аналогии
f"Жалоба на контент: аккаунт {Chelovek} распространяет ненормативную лексику",
f"Нарушение правил: аккаунт {Chelovek} размещает запрещенный контент",
f"Жалоба: аккаунт {Chelovek} проводит дезинформацию и манипуляции",
f"Жалоба на контент: аккаунт {Chelovek} распространяет нелегальные материалы",
f"Нарушение правил: аккаунт {Chelovek} пропагандирует насилие и экстремизм",
f"Жалоба: аккаунт {Chelovek} нарушает авторские права и пиратство",
f"Жалоба на контент: аккаунт {Chelovek} размещает порнографию",
f"Нарушение правил: аккаунт {Chelovek} проводит финансовые мошенничества",
f"Жалоба: аккаунт {Chelovek} нарушает законы о защите личных данных",
f"Жалоба на контент: аккаунт {Chelovek} распространяет ложную информацию",
f"Жалоба на контент: аккаунт пропагандирует наркотики и нарушает законы",
f"Нарушение правил: аккаунт размещает угрозы и вызывает ненависть к определенной группе людей",
f"Жалоба: аккаунт нарушает правила конфиденциальности и собирает личные данные без согласия",
f"Жалоба на контент: аккаунт распространяет дезинформацию о пандемии и вакцинах",
f"Нарушение правил: аккаунт использует религиозную риторику для манипуляции и пропаганды",
f"Жалоба: аккаунт размещает контент, нарушающий права детей и подростков",
f"Жалоба на контент: аккаунт распространяет фейки о политических событиях",
f"Нарушение правил: аккаунт проводит кибербуллинг и угрожает безопасности других пользователей",
f"Жалоба: аккаунт нарушает этические нормы и создает враждебную атмосферу в сети",
f"Жалоба на контент: аккаунт размещает материалы, пропагандирующие самоповреждения и суицид",
f"Content complaint: {Chelovek} account spreads profanity.",
f"Violation of rules: {Chelovek} account posts prohibited content.",
f"Complaint: {Chelovek} account is engaging in misinformation and manipulation",
f"Content complaint: {Chelovek} account is distributing illegal content",
f"Violation of rules: {Chelovek} account promotes violence and extremism",
f"Complaint: {Chelovek} account violates copyright and piracy.",
f"Content complaint: {Chelovek} account is posting pornography.",
f"Violation of rules: account {Chelovek} is conducting financial fraud.",
f"Complaint: {Chelovek} account violates privacy laws.",
f"Content complaint: {Chelovek} account is spreading false information",
f"Content complaint: account promotes drugs and violates laws.",
f"Violation of rules: account posts threats and incites hatred towards a certain group of people.",
f"Complaint: account violates privacy rules and collects personal data without consent",
f"Content complaint: account spreads misinformation about pandemic and vaccines.",
f"Violation of rules: account uses religious rhetoric to manipulate and propagandize.",
f"Complaint: account posts content that violates the rights of children and adolescents",
f"Content complaint: account spreads fakes about political events.",
f"Violation of rules: account is cyberbullying and jeopardizing the safety of other users",
f"Complaint: account violates ethical norms and creates a hostile atmosphere online.",
f"Content complaint: the account posts materials that promote self-harm and suicide"
]
for senderemail, senderpassword in senders:
    for recipientemail in recipients:
        subject = random.choice(subjects)
        messagetext = random.choice(messages)
        sendemail(senderemail, senderpassword, recipientemail, subject, messagetext)
        timeSleep = random.randint(60, 180)
        time.sleep(timeSleep)

