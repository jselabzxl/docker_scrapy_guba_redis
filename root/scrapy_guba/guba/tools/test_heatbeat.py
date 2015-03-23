# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Filename:    test_heatbeat.py
# Revision:    1.0
# Date:        2014-10-22
# Author:      LinHaoBuaa
# web:         https://github.com/linhaobuaa/
# Email:       linhao.lh@qq.com
# -------------------------------------------------------------------------------
import pexpect
import time
import datetime
import smtplib
from email.mime.text import MIMEText
from test_network import test_network

# base set
# 配置要监测的IP地址, 使用baidu的IP
check_ip ={"119.75.217.56": 0}

# 定义几次ping不通发邮件
send_mail_limit = [3, 4]
verify_network_limit = 1

# 发邮件的邮件服务器配置
mail_host = "smtp.qq.com"
mail_user = "linhao.lh@qq.com"
mail_pwd = "linhao822851"
mail_to = "1257819385@qq.com"
mail_cc = "294799356@qq.com"

def mail_warn(error_ip):
    content = 'Ping IP %s is error!' % error_ip
    msg = MIMEText(content)
    msg['From'] = mail_user
    msg['Subject'] = 'warnning %s' % error_ip
    msg['To'] = mail_to

    try:
	s = smtplib.SMTP()
	s.connect(mail_host)
	s.login(mail_user, mail_pwd)
	s.sendmail(mail_user, [mail_to, mail_cc], msg.as_string())
        s.close()
    except Exception, e:
        print e


def check(get_ip):
    try :
        ping = pexpect.spawn("ping -c1 %s" % (get_ip))
        check_result = ping.expect([pexpect.TIMEOUT, "1 packets transmitted, 1 received, 0% packet loss"], 2)
    except :
        check_result = 0

    return check_result


def main():
    while True:
        for i in check_ip:
            check_status = check("%s" % i)
            if check_status == 1:
                check_ip["%s"%i] = 0
            else:
                check_ip["%s"%i] += 1

            if check_ip["%s"%i] >= verify_network_limit:
                test_network()
                check_ip["%s"%i] = 0
            else:
                print datetime.datetime.now(), 'test network success' 

        time.sleep(1)


if __name__ == "__main__":
    main()
