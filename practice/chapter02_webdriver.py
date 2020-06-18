# ** chapter00_webdriver.py
# * selenium의 webdriver 사용방법(*chrome driver)
# *

from selenium import webdriver

#instagrm 페이지에서 원하는 해쉬태그로 selenium 접속 (+ 크롬 드라이버)
driver = webdriver.Chrome(executable_path='../webdriver/chromedriver.exe') #상대주소 :내기준으로 찾아가는것.

#https://www.instagram.com/explore/tags/%ED%94%BC%EA%B7%9C%EC%96%B4/
# url 주소의 한글은 유니코드로 변환( 한글 이면 깨지는 경우가 있음)
url = 'https://www.instagram.com/explore/tags/%ED%94%BC%EA%B7%9C%EC%96%B4/'
driver.get(url)
# driver.close()  # 실행 후 브라우저 종료
