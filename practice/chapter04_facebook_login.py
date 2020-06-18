 # ** chapter04_facebook_login.py
 # * selenium을 이용해서 페이스북 로그인
 # * : 지속적으로 사용 불가능.. 페이스북이 보안을 위해 로그인버튼의
 # * 선택지를 수시로 변경함 OTL...

from selenium import webdriver

 # selenium을 사용해서 facebook에 로그인!
 # !!로그인 버튼은 보안조치 때문에 id값이 자꾸 변동함
path = '..'
driver = webdriver.Chrome(executable_path='{}/webdriver/chromedriver.exe'.format(path))

url = 'http://www.facebook.com/'
driver.get(url)
driver.find_element_by_id('email').send_keys('')
driver.find_element_by_id('pass').send_keys('')
driver.find_element_by_id('u_o_e').click() # 로그인 버튼 id값이 보안때문에 수시로 변경됨



