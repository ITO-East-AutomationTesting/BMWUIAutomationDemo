# coding=utf-8
import os
import smtplib
import os.path
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:
    # 定义邮件内容
    def email_init(self, report, reportName):
        with open(report, 'rb') as file:
            mail_body = file.read()

        # 创建一个带附件的邮件实例
        msg = MIMEMultipart()
        # 测试报告作为邮件正文
        msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
        report_file = MIMEText(mail_body, 'html', 'utf-8')
        # 定义附件名称
        report_file["Content-Disposition"] = 'attachment;filename=' + reportName
        # 添加附件
        msg.attach(report_file)
        # 邮件标题
        msg['Subject'] = 'APP自动化测试报告：' + reportName
        # 发件人
        msg['From'] = '775881448@qq.com'
        # 收件人 email_to = 'aa@qq.com;bb@qq.com'
        msg['To'] = '775881448@qq.com'
        try:
            server = smtplib.SMTP_SSL("smtp.qq.com",465)
            server.login('775881448@qq.com', 'tyqhamzuaajabdib')
            server.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
            server.quit()
        except smtplib.SMTPException:
            logging.info(u'邮件发送测试报告失败 at' + __file__)

    def sendReport(self):
        # 找到最新的测试报告
        base_dir = os.path.dirname(os.path.dirname(__file__))
        reportFilePath = os.path.join(base_dir, 'reports')
        report_list = os.listdir(reportFilePath)
        report_list.sort(key=lambda fn: os.path.getatime(reportFilePath + '\\' + fn))

        new_report = os.path.join(reportFilePath, report_list[-1])
        self.email_init(new_report, report_list[-1])
        # SendEmail(new_report, report_list[-1])


# if __name__ == '__main__':
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # reportFilePath = os.path.join(base_dir, 'reports')
    # report_list = os.listdir(reportFilePath)
    # report_list.sort(key=lambda fn: os.path.getatime(reportFilePath + '\\' + fn))
    #
    # new_report = os.path.join(reportFilePath, report_list[-1])
    # # self.__init__(new_report, report_list[-1])
    # SendEmail(new_report, report_list[-1])
