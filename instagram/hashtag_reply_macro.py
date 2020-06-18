# * 해시태그 피드에 좋아요와 댓글을


from selenium import webdriver
import time
from bs4 import BeautifulSoup
import random
# 1.Chromer driver setup
path = '..'
driver = webdriver.Chrome(executable_path='{}/webdriver/chromedriver.exe'.format(path))

# 2. instagram Login

url = 'https://www.instagram.com/accounts/login/?next=%2Fexplore%2Ftags%2F%ED%94%BC%EA%B7%9C%EC%96%B4%2F&source=desktop_nav'
driver.get(url)
time.sleep(3)

# what is xpath?
# : xpath는 w3c의 표준으로 확장 생성언어 문서와 구조를 통해 경로 위에
# 지정한 구문을 사용하여 항목을 배치하고 처리하는 방법을 기술하는 언어
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys('')
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys('') #패스워드
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click() # 로그인버튼 클릭

# 3. HashTag Searching
time.sleep(2)
hash_url = 'https://www.instagram.com/explore/tags/%ED%94%BC%EA%B7%9C%EC%96%B4/'
driver.get(hash_url)

# 4. Board List Input & output
def parse(page_code):
    soup = BeautifulSoup(page_code,'html.parser')
    feed_list = soup.findAll('div',{'class','v1Nh3'}) # class 값은 수시로 변경됨(실행할때)


    links = []
    for one in feed_list:
        insta_link = 'https://www.instagram.com'
        link_addr = one.find('a')['href']
        print(insta_link + link_addr)
        links.append(insta_link +link_addr)
    return links

time.sleep(4)
page_code = driver.page_source
links = parse(page_code)
print('Feed Cnt:', len(links))

# 좋아요 누르고 댓글 달기
for url in links:
    try:
        driver.get(url)

        rnd_sec = random.randint(5,15)
        time.sleep(rnd_sec)
        message = '피규어:)'
        #좋아요 누르고 댓글 달기
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
        #댓글
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div[3]/div/form/textarea').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div[3]/div/form/textarea').click()
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div[3]/div/form/textarea').click()



    except Exception as e:
        print(e)




