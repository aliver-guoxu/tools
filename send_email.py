import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

sender='nengyuanguoxu@163.com'
recivers=['nengyuanguoxu@126.com','dushanshan2011@126.com','quinn.du@philips.com']
password='***************' #这里填写开启认证的密码

def email(reciver):
    ret='ok'
    try:
        text='亲爱的{}' \
             '我在这儿等着你回来，等着你回来把那桃花开'.format(reciver)
        msg=MIMEText(text)
        msg['Form']=formataddr(['',sender])
        msg['To']=formataddr(['',reciver])
        msg['Subject']='这是{}发给您的邮件'.format(sender)

        server=smtplib.SMTP('smtp.163.com',25)
        server.login(sender,password)
        server.sendmail(sender,[reciver,],msg.as_string())
        server.quit()
    except:
        ret='fail'
    return ret

if __name__ == '__main__':
    for reciver in recivers:
        result=email(reciver)
        if result == 'ok':
            print('发往{}的邮件发送成功'.format(reciver))
        else:
            print('发送失败')
