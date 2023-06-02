import smtplib
from email.mime.text import MIMEText
from email.header import Header
from Django_test.common.loggin import logger

"""
邮件通知
 from_mail  : 邮件收件人
 to_mail_list ：邮件发送人
 note_content : 文件内容"""

mail_host = ""  # 服务器地址
mail_user = ""  # 用户名
mail_pass = ""  # 口令


def send_mails_lavalhost(receivers=[mail_user], subject="", content=""):
    """
    @param:
    receivers	list	邮件接收方的邮箱列表， eg. ['****@qq.com', '*****@163.com']
    subject		str		发送的邮件主题
    content		str		发送的邮件内容
    """
    msg = MIMEText(content, "plain", "utf-8")
    msg["From"] = MIMEText("complate", "utf-8")
    msg["To"] = MIMEText("test", "utf-8")
    try:
        smtObj = smtplib.SMTP
        smtObj.connect(mail_host, 25)
        smtObj.login(mail_user, mail_pass)
        smtObj.sendmail(receivers, subject, msg.as_string())
        logger.info("邮件发送成功，收件人：｛｝".format(receivers))
    except smtplib.SMTPException:
        logger.debug("邮件发送失败，失败原因｛｝".format(smtplib.SMTPException))
