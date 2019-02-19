from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from twilio.rest import Client

browser = webdriver.Chrome()
# 购票日期
buyTicketDay = '2019-02-22'
# 购票人
person = "***"
queryYZ = ''
queryWZ = ''


def send_mail(notestr):  # 邮箱通知

    msg = MIMEText(notestr, 'plain', 'utf-8')
    subject = '抢票结果通知'
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = 'Tomm<发件人邮箱>'
    msg['To'] = "收件人邮箱"

    # 输入Email地址和口令:
    from_addr = '发件人邮箱'
    password = '***'  # 不是登录密码，而是客户端授权码
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'
    # 输入收件人地址:
    to_addr = '收件人邮箱'

    server = smtplib.SMTP()  # SMTP协议默认端口是25
    server.connect(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


def send_message(noteStr):  # 短信通知

    account_sid = 'ACc8dddd69ae80c69f816f5cb24c6a0cca'
    auth_token = '***'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+发短信人手机号',
        body=noteStr,#短信内容
        to='+86收短信手机号'
    )


def submit_order():  # 完成提交订单一系列功能

    time.sleep(5)
    browser.find_element_by_xpath('//div[@class="content"]//div[@class="per-sel"]//ul[@id="normal_passenger_id"]'
                                  '/li/label[text()=person]/../input').click()
    # 购买学生票,如果选择否，将.dialog_xsertcj_ok改为dialog_xsertcj_cancel
    # 针对乘客信息里包含"(学生)"的乘客，其他乘客则直接注释掉下面一行代码
    time.sleep(1)
    browser.find_element_by_css_selector('#body_id #dialog_xsertcj .up-box-bd .lay-btn .dialog_xsertcj_ok').click()

    # 提交订单
    time.sleep(2)
    browser.find_element_by_xpath('//div[@class="content"]//div[@class="lay-btn"]/a[@id="submitOrder_id"]').click()

    # 核对信息
    time.sleep(2)
    browser.find_element_by_css_selector('.dhtmlx_window_active .dhtmlx_wins_body_inner .dhtmlx_wins_no_header'
                                         '#checkticketinfo_id .up-box-bd.ticket-check #confirmDiv #qr_submit_id'
                                         ).click()


def refresh_order():
    try:

        browser.get('https://kyfw.12306.cn/otn/leftTicket/init')
        # 通过添加cookie的方式实现起终站以及购票时间的输入
        browser.add_cookie({'name': '_jc_save_fromStation', 'value': '%u6F62%u5DDD%2CKCN'})
        browser.add_cookie({'name': '_jc_save_toStation', 'value': '%u90D1%u5DDE%2CZZF'})
        browser.add_cookie({'name': '_jc_save_fromDate', 'value': buyTicketDay})

        js = 'window.open("https://kyfw.12306.cn/otn/resources/login.html");'
        browser.execute_script(js)
        handles = browser.window_handles
        # 暂停120秒去登录
        time.sleep(120)
        # 然后切换到抢票界面
        browser.switch_to.window(handles[0])

        time.sleep(3)
        browser.refresh()
        click_query = browser.find_element_by_css_selector('.content.content-lg .sear-box.quick-sear-box.sear-box-lg '
                                                           '.quick-s .btn-area a')
        time.sleep(3)
        # index用于统计抢票次数
        index = 0
        while True:
            click_query.click()
            time.sleep(10)
            try:
                global queryWZ, queryYZ
                queryYZ = browser.find_element_by_css_selector('.content.content-lg .t-list #queryLeftTable '
                                                               '#ticket_580000K7440O #YZ_580000K7440O').text
                queryWZ = browser.find_element_by_css_selector('.content.content-lg .t-list #queryLeftTable '
                                                               '#ticket_580000K7440O #WZ_580000K7440O').text
            finally:
                pass
            if (queryYZ != '无' and queryYZ != '--') or (queryWZ != '无' and queryWZ != '--'):
                browser.find_element_by_css_selector('.content.content-lg .t-list #queryLeftTable '
                                                     '#ticket_580000K7440O td').click()
                noteStr = "有硬座或者无座，及时查看"
                send_mail(noteStr)
                send_message(noteStr)
                try:
                    submit_order()
                except Exception as e:
                    print(e)
                    print("提交订单失败")
                    send_message("有余票但是提交订单失败")
                finally:
                    pass
                index = index+1
                print("第"+str(index)+"次抢票结果： 成功")
                break
            index = index+1
            print("第"+str(index)+"次抢票结果: 失败")

    finally:
        print("Something is wrong")
        send_message("程序运行出错")


if __name__ == "__main__":
    refresh_order()
