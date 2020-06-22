import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from requests.cookies import RequestsCookieJar
from lxml import html
import pickle


def jd_login(username, password):
    # 路径一定要正斜杠，反斜杠会找不到文件
    driver = webdriver.Chrome('D:/dev/tools/driver/chromedriver_win32/chromedriver.exe')
    # driver = webdriver.Chrome()
    driver.get('https://passport.jd.com/new/login.aspx')  # JD 登录页面
    time.sleep(2)  # 等待加载
    driver.find_element_by_css_selector('div.login-tab-r a').click()     # 切换登录按钮
    driver.find_element_by_css_selector('input#loginname').send_keys(username)   # 填写账号
    driver.find_element_by_css_selector('input#nloginpwd').send_keys(password)      # 填写密码
    driver.find_element_by_css_selector('a#loginsubmit').click()              # 点击登录按钮
    # driver.delete_all_cookies()
    time.sleep(15)  # 等待加载
    jd_cookies = driver.get_cookies()
    driver.close()  # 关闭浏览器
    pickle.dump(jd_cookies, open('d:/cookies.pkl', 'wb'))  # 保存cookies
    print('cookies save successfully!')


def go_page(url):
    session = webdriver.Chrome('D:\dev\tools\driver\chromedriver_win32\chromedriver.exe')
    cookies = pickle.load(open("d:/cookies.pkl", "rb"))
    session.get(url)
    session.delete_all_cookies()
    for c in cookies:
        new = dict(c, **{
            "domain": ".jd.com",
            "expires": "",
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False,
        })
        session.add_cookie(new)
    session.get(url)


def download_page(url):
    cookies = pickle.load(open("d:/cookies.pkl", "rb"))
    print(cookies)
    cookie_jar = RequestsCookieJar()
    for c in cookies:
        cookie_jar.set(c['name'], c['value'], domain="jd.com")
    page = requests.get(url,cookies=cookie_jar)
    soup = BeautifulSoup(page.text, 'html.parser', from_encoding='utf-8')
    print(soup.getText())
    print(page)
    print('爬取成功')


jd_login('18101356283','huxia0feng')
# go_page('https://trade.jr.jd.com/centre/browse.action')
download_page('https://trade.jr.jd.com/centre/browse.action')


