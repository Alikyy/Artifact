from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle,os
import time
from datetime import datetime

#情報
login_url = 'https://vrchat.com/home/login' # ログインのページ
web_url = 'https://vrchat.com/home/worlds' # 入りたいページ
username = 'hogehogeID' # ユーザーの名前
password = 'hogehogepw' # パスワード
cookies_file = 'PWFILE.pkl' # クッキーを保存するファイルの名前
#'PWFILE.pkl' の保存先 %USERPROFILE%

# ChromeのGUIを開かず実行
"""
chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(options=chrome_options)
"""
#ChromeのGUIを開いて実行
driver = webdriver.Chrome()

# まだクッキーを持っていない場合新しくログインして保存する
if(not os.path.exists(cookies_file)):
    driver.get(login_url)
    name_box = driver.find_element(By.ID,'username_email')
    name_box.send_keys(username)
    password_box = driver.find_element(By.NAME, 'password')
    password_box.send_keys(password)
    remember_box = driver.find_element(By.CLASS_NAME, 'tw-mt-6')
    remember_box.click()
    time.sleep(60)
    cookies = driver.get_cookies()
    pickle.dump(cookies,open(cookies_file,'wb'))
    
# すでにクッキーを持っている場合読み込んで使う
else:
    cookies = pickle.load(open(cookies_file,'rb'))
    driver.get(web_url)
    for c in cookies:
        driver.add_cookie(c)

# VRC公式サイトを開く
driver.get(web_url)
driver.implicitly_wait(10)

#Trending WorldDate更新
for i in range(12):
    world_add = driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .css-5lomjw > .right-world-nav .svg-inline--fa").click()
    time.sleep(1)

# CSSセレクターを使って要素のHTMLを取得
page_source = driver.page_source

#1番目画像なしホーム名+人数
elements = driver.find_elements(By.CSS_SELECTOR, "div:nth-child(2) > .css-5lomjw > .css-11f1sih > div:nth-child(n+1):nth-child(-n+30) .tw-flex.tw-flex-row.tw-justify-between")

# 複数の要素をHTMLとして連結
element_html = ""
for element in elements:
    element_html += element.get_attribute("outerHTML") + "\n"

# 保存するファイルのパスを指定
current_date = datetime.now().strftime("%Y_%m%d_%H%M")
save_directory = "出力先"
save_path = os.path.join(save_directory, current_date + '.html')

# 取得したHTMLをファイルに保存
with open(save_path, "w", encoding="utf-8") as file:
    file.write(element_html)