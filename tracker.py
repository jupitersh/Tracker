#!/usr/bin/python3

import os, re, json, sys
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTPException
from smtplib import SMTP_SSL

# 邮件相关
host_server = 'smtp.qq.com'
sender = sys.argv[1] # QQ号
password = sys.argv[2] # QQ邮箱SMPT授权码，注意，不是QQ邮箱的登录密码

SteamID = sys.argv[4] # 填被追踪的人的SteamID

def SendEmail(receiver, mail_title, mail_content):
    try:
        smtp = SMTP_SSL(host_server)
        smtp.set_debuglevel(0) # 参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.ehlo(host_server)
        smtp.login(sender, password)

        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender + '@qq.com'
        msg["To"] = receiver
        smtp.sendmail(sender + '@qq.com', receiver, msg.as_string())
        smtp.quit()
        print('邮件 %s 发送成功，内容：%s' % (mail_title, mail_content[:50]))
    except SMTPException as e:
        print('Error: ', e)

text = '''
token='%s'
servers=(us eu china sing)
for i in ${servers[*]}
do
  curl -k -X POST -d \
  '{"__gameId":"DontStarveTogether","__token":"'${token}'","query":{}}' \
  https://lobby-${i}.kleientertainment.com/lobby/read > \
  dst_${i}.json
done
''' % sys.argv[5]

with open('test.sh', 'w') as f:
    f.write(text)

os.system('chmod +x test.sh && bash test.sh')

file_suffix = ['us', 'eu', 'china', 'sing']

for suffix in file_suffix:
    #print(suffix, os.path.getsize('dst_%s.json' % suffix)/1024/1024)
    with open('dst_%s.json' % suffix, 'r') as f:
        content = f.read()
        #print(content)
        if SteamID in content:
            results = re.findall('"name":"(.*?)".*?"players":(.*?),"steamid"', content)
            for result in results:
                if SteamID in result[1]:
                    print(result[0])
                    SendEmail(sys.argv[3], '被追踪者已上线', '服务器名：%s' % result[0])
        if len(content) < 50:
            SendEmail(sys.argv[3], '追踪出错', content)
            break
