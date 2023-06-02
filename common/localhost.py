import smtplib
from email.mime.text import MIMEText
from email.header import Header
from Django_test.common.loggin import logger

mail_host = "smtp.qq.com"  # 服务器地址
mail_user = "1258881069@qq.com"  # 用户名
mail_pass = "123123"  # 口令


def send_mails_lavalhost(receivers=[mail_user], subject="", content=""):
    """
    @param:
    receivers	list	邮件接收方的邮箱列表， eg. ['****@qq.com', '*****@163.com']
    subject		str		发送的邮件主题
    content		str		发送的邮件内容
    """
    if receivers is None:
        receivers = [mail_user]
    msg = MIMEText(content, "plain", "utf-8")
    msg["From"] = Header("complate", "utf-8")
    msg["To"] = Header("test", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    try:
        smtObj = smtplib.SMTP
        smtObj.connect(mail_host, 25)  # 25 为smtp服务的端口号
        smtObj.login(mail_user, mail_pass)
        smtObj.sendmail(mail_user, receivers, msg.as_string())
        logger.info("邮件发送成功，收件人：｛｝".format(receivers))
    except smtplib.SMTPException:
        logger.debug("邮件发送失败，失败原因｛｝".format(smtplib.SMTPException))
