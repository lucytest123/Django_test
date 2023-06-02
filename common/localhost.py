import smtplib
from email.mime.text import MIMEText
from email.header import Header
from Django_test.common.loggin import logger

"""
邮件通知
 from_mail  : 收件人
 to_mail_list ：抄送人
 note_content : 文件内容"""


def send_mails_lavalhost(from_mail, to_mail_list, note_content):
    msg = MIMEText(note_content, "plain", "utf-8")
    with smtplib.SMTP("localhost") as smtObj:
        smtObj.sendmail(from_mail, to_mail_list, msg.as_string())
        logger.info("邮件发送成功，收件人：｛｝".format(to_mail_list))
