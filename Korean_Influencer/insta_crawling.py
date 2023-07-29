# step1.필요한 패키지와 모듈 불러오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# step2.아이디, 비밀번호 설정
id = "여러분의 아이디를 입력해주세요"
pw = "여러분의 비밀번호를 입력해주세요"

# step3.크롬 웹드라이버 실행
driver = webdriver.Chrome(r"C:\Users\SANGWOO\Desktop\chromedriver.exe")

# step4.인스타그램 로그인 함수 정의
def login(id, pw):
    # 로그인 페이지로 이동
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
    
    # id와 pw를 입력하는 창의 요소 정보 획득
    input = driver.find_elements_by_tag_name("input")

    # 아이디를 입력
    input[0].send_keys(id)

    # 비밀번호 입력
    input[1].send_keys(pw)

    # 엔터
    input[1].send_keys(Keys.RETURN)
    time.sleep(5)

    # 로그인 정보 저장 여부 팝업창 제거 ("나중에 하기 버튼 클릭")
    btn_later1 = driver.find_element_by_class_name('_acan._acao._acas')
    btn_later1.click()
    time.sleep(5)

    # 알림 설정 팝업창 제거 ("나중에 하기 버튼 클릭")
    btn_later2 = driver.find_element_by_class_name('_a9--._a9_1')
    btn_later2.click()

# step5.로그인 함수 실행
login(id,pw)
