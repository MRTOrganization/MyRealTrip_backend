import os
from urllib import parse

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Flight:
    def __init__(self, origin_k, destination_k, depart_date, return_date):
        self.origin_k = origin_k
        self.destination_k = destination_k
        self.depart_date = depart_date
        self.return_date = return_date



    def search_flight(self):
        city_korean_dict = {
            '인천':'ICN',
            '김포':'GMP',
            '제주':'CJU',
            '부산':'PUS',
            '오사카':'OSA',
            '도쿄':'TYO',
            '후쿠오카':'FUK',
            '삿포로':'SPK',
            '북경':'BJS',
            '상해/푸동':'PVG'
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

        driver = webdriver.Chrome('../chromedriver')
        driver.implicitly_wait(10)

        url = f'http://flights.myrealtrip.com/air/b2c/AIR/INT/AIRINTSCH0100100010.k1?initform=RT&domintgubun=I&depctycd={origin}&depctycd={destination}&depctycd=&depctycd=&depctynm={origin_k}&depctynm={destination_k}&depctynm=&depctynm=&arrctycd={destination}&arrctycd={origin}&arrctycd=&arrctycd=&arrctynm={destination_k}&arrctynm={origin_k}&arrctynm=&arrctynm=&depdt={depart_date}&depdt={return_date}&depdt=&depdt=&opencase=N&opencase=N&opencase=N&openday=&openday=&openday=&depdomintgbn=I&tasktype=B2C&servicecacheyn=Y&adtcount=1&chdcount=0&infcount=0&cabinclass=Y&cabinsepflag=Y&preferaircd=&secrchType=FARE&maxprice=&availcount=250&KSESID=air%3Ab2c%3ASELK138RB%3ASELK138RB%3A%3A00'
        driver.get(url)

        # try:
        #     title = WebDriverWait(driver, 10) \
        #         .until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div#k1_container")))
        #     print(title)
        # finally:
        #     driver.quit()
        # print(url)
        flight_info_list = list()
        result_list = driver.find_elements_by_css_selector("li[role='resultLi']")
        for result in result_list:

            list_class = result.find_elements_by_css_selector('div.list')

            # 출발편
            go_airline =list_class[0].find_element_by_css_selector('span.airline_name').text
            go_dep_time = list_class[0].find_element_by_css_selector('span.dep_time > span').text[:5]
            go_dep_airport = list_class[0].find_element_by_css_selector('span.dep_time > span > em').text
            go_flytime = list_class[0].find_element_by_css_selector('span.from_to > em.time').text
            go_arr_time = list_class[0].find_element_by_css_selector('span.arr_time > span.plus_day > span').text
            go_arr_airport = list_class[0].find_element_by_css_selector('span.arr_time > span > em').text

            # 귀국편
            return_airline = list_class[1].find_element_by_css_selector('span.airline_name').text
            return_dep_time = list_class[1].find_element_by_css_selector('span.dep_time > span').text[:5]
            return_dep_airport = list_class[1].find_element_by_css_selector('span.dep_time > span > em').text
            return_flytime = list_class[1].find_element_by_css_selector('span.from_to > em.time').text
            return_arr_time = list_class[1].find_element_by_css_selector('span.arr_time > span.plus_day > span').text
            return_arr_airport = list_class[1].find_element_by_css_selector('span.arr_time > span > em').text

            # 가격
            price = result.find_element_by_css_selector('span#bottomClose').text
            new_flightinfo = FlightInfo(
                go_airline=go_airline,
                go_dep_time=go_dep_time,
                go_dep_airport=go_dep_airport,
                go_flytime=go_flytime,
                go_arr_time=go_arr_time,
                go_arr_airport=go_arr_airport,
                return_airline=return_airline,
                return_dep_time=return_dep_time,
                return_dep_airport=return_dep_airport,
                return_flytime=return_flytime,
                return_arr_time=return_arr_time,
                return_arr_airport=return_arr_airport,
                price=price
            )
            flight_info_list.append(new_flightinfo)
        return flight_info_list


class FlightInfo:
    def __init__(self, go_airline, go_dep_time, go_dep_airport, go_arr_time, go_arr_airport, go_flytime,
                 return_airline, return_dep_time, return_dep_airport, return_arr_time, return_arr_airport, return_flytime, price):
        self.go_airline = go_airline
        self.go_dep_time = go_dep_time
        self.go_dep_airport = go_dep_airport
        self.go_arr_time = go_arr_time
        self.go_arr_airport =go_arr_airport
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
