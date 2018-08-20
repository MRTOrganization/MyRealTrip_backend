import os
from urllib import parse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Flight:
    def __init__(self, origin_k, destination_k, depart_date, return_date):
        self.origin_k = origin_k
        self.destination_k = destination_k
        self.depart_date = depart_date
        self.return_date = return_date

    def search_flight(self):

        # 한글도시 : 영문도시 딕셔너리
        city_korean_dict = {
            '인천': 'ICN',
            '김포': 'GMP',
            '제주': 'CJU',
            '부산': 'PUS',
            '오사카': 'OSA',
            '도쿄': 'TYO',
            '후쿠오카': 'FUK',
            '삿포로': 'SPK',
            '북경': 'BJS',
            '상해/푸동': 'PVG'
        }
        origin_k = self.origin_k
        destination_k = self.destination_k
        origin = city_korean_dict[origin_k]
        destination = city_korean_dict[destination_k]

        # yyyy-mm-dd 형식으로 입력
        depart_date = self.depart_date
        return_date = self.return_date

        # 한글 url 파싱
        origin_k = parse.quote(origin_k)
        destination_k = parse.quote(destination_k)
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--dump-dom")

        # runserver
        dirs = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chromedriver')
        # dirs = webdriver.Chrome(executable_path=dirs, chrome_options=chrome_options)
        # deploy
        # dirs = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'chromedriver_linux')
        # driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
        print(dirs)
        driver = webdriver.Chrome(executable_path=dirs, chrome_options=chrome_options)
        driver.implicitly_wait(15)
        # url
        url = f'http://flights.myrealtrip.com/air/b2c/AIR/MBL/AIRMBLSCH0100100010.k1?initform=RT&domintgubun=I&depctycd={origin}&depctycd={destination}&depctycd=&depctycd=&depctynm={origin_k}&depctynm={destination_k}&depctynm=&depctynm=&arrctycd={destination}&arrctycd={origin}&arrctycd=&arrctycd=&arrctynm={destination_k}&arrctynm={origin_k}&arrctynm=&arrctynm=&depdt={depart_date}&depdt={return_date}&depdt=&depdt=&opencase=N&opencase=N&opencase=N&openday=&openday=&openday=&depdomintgbn=I&tasktype=B2C&servicecacheyn=Y&adtcount=1&chdcount=0&infcount=0&cabinclass=Y&cabinsepflag=Y&preferaircd=&secrchType=FARE&maxprice=&availcount=250&KSESID=air%3Ab2c%3ASELK138RB%3ASELK138RB%3A%3A00'

        driver.get(url)

        flight_info_list = list()


        # role속성이 resultLi인 리스트 결과를 가져옴
        result_list = driver.find_elements_by_css_selector("li[role='resultLi']")

        for result in result_list:
            flight_info_dict = dict()
            list_class = result.find_elements_by_css_selector('div.list')
            # flight_info_dict에 키와 값을 넣음
            # 출발편
            flight_info_dict["go_airline"] = list_class[0].find_element_by_css_selector('span.airline_name').text
            flight_info_dict["go_dep_time"] = list_class[0].find_element_by_css_selector('span.dep_time > span').text[
                                              :5]
            flight_info_dict["go_dep_airport"] = list_class[0].find_element_by_css_selector(
                'span.dep_time > span > em').text
            flight_info_dict["go_flytime"] = list_class[0].find_element_by_css_selector('span.from_to > em.time').text
            flight_info_dict["go_arr_time"] = list_class[0].find_element_by_css_selector(
                'span.arr_time > span.plus_day > span').text
            flight_info_dict["go_arr_airport"] = list_class[0].find_element_by_css_selector(
                'span.arr_time > span > em').text

            # 귀국편
            flight_info_dict["return_airline"] = list_class[1].find_element_by_css_selector('span.airline_name').text
            flight_info_dict["return_dep_time"] = list_class[1].find_element_by_css_selector(
                'span.dep_time > span').text[:5]
            flight_info_dict["return_dep_airport"] = list_class[1].find_element_by_css_selector(
                'span.dep_time > span > em').text
            flight_info_dict["return_flytime"] = list_class[1].find_element_by_css_selector(
                'span.from_to > em.time').text
            flight_info_dict["return_arr_time"] = list_class[1].find_element_by_css_selector(
                'span.arr_time > span.plus_day > span').text
            flight_info_dict["return_arr_airport"] = list_class[1].find_element_by_css_selector(
                'span.arr_time > span > em').text

            # 가격
            flight_info_dict["price"] = result.find_element_by_css_selector('span#bottomClose').text
            # flight_info_dict를 flight_info_list의 원소로 삽입
            flight_info_list.append(flight_info_dict)
        return flight_info_list


class FlightInfo:
    def __init__(self, go_airline, go_dep_time, go_dep_airport, go_arr_time, go_arr_airport, go_flytime,
                 return_airline, return_dep_time, return_dep_airport, return_arr_time, return_arr_airport,
                 return_flytime, price):
        self.go_airline = go_airline
        self.go_dep_time = go_dep_time
        self.go_dep_airport = go_dep_airport
        self.go_arr_time = go_arr_time
        self.go_arr_airport = go_arr_airport
        self.go_flytime = go_flytime
        self.return_airline = return_airline
        self.return_dep_time = return_dep_time
        self.return_dep_airport = return_dep_airport
        self.return_arr_time = return_arr_time
        self.return_arr_airport = return_arr_airport
        self.return_flytime = return_flytime
        self.price = price

#
# icn2osa = Flight('인천', '오사카','2018-08-24', '2018-08-30')
# icn2osa.search_flight()
