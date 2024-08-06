import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import time

def enviar_emails(smtp_server, smtp_port, smtp_user, smtp_password, subject, body, recipients, delay=10):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)

    for index, recipient in enumerate(recipients):
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(smtp_user, recipient, msg.as_string())

        if (index + 1) % 10 == 0:
            print(f"Enviados {index + 1} e-mails. Aguardando {delay} segundos.")
            time.sleep(delay)

    server.quit()
    print('E-mails enviados com sucesso!')

def carregar_recipientes(arquivo_csv):
    df = pd.read_csv(arquivo_csv)
    return df['email'].tolist()

def menu():
    print("Menu:")
    print("1. Enviar e-mails")
    print("2. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        smtp_server = input("Servidor SMTP: ")
        smtp_port = int(input("Porta SMTP: "))
        smtp_user = input("E-mail do remetente: ")
        smtp_password = input("Senha do e-mail: ")
        subject = input("Assunto do e-mail: ")
        body = input("Corpo do e-mail: ")
        arquivo_csv = input("Caminho para o arquivo CSV com endereços de e-mail: ")

        recipients = carregar_recipientes(arquivo_csv)
        enviar_emails(smtp_server, smtp_port, smtp_user, smtp_password, subject, body, recipients)
    elif escolha == '2':
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")
        menu()

if __name__ == "__main__":
    menu()
