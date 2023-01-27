#네이버 검색광고 API 사용하기 sample

import time
import random
import requests
import pandas as pd
import signaturehelper


def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(round(time.time() * 1000))
    signature = signaturehelper.Signature.generate(
        timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8',
            'X-Timestamp': timestamp, 'X-API-KEY': API_KEY,
            'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}


BASE_URL = 'https://api.naver.com'
method = "GET"

uri = '/keywordstool'
API_KEY = "0100000000e90c570d48dfd82273fdf0bbed2b56a6a241e5b76186e2d63aa5745fef8db0f6"
SECRET_KEY = "AQAAAADpDFcNSN/YInP98LvtK1amFvFUBVQfRj7oYU1KtnBm2g=="
CUSTOMER_ID = "2781326"

r = requests.get(BASE_URL + uri+'?hintKeywords={}&showDetail=1'.format(input('연관키워드를 조회할 키워드를 입력!!!\n')),
                 headers=get_header(method, uri, API_KEY, SECRET_KEY, CUSTOMER_ID))

r.json()['keywordList'][0]

df = pd.DataFrame(r.json()['keywordList'])
df.head()

df.rename({'compIdx': '경쟁정도', 'monthlyAveMobileClkCnt': '월평균클릭수_모바일',
           'monthlyAveMobileCtr': '월평균클릭률_모바일', 'monthlyAvePcClkCnt': '월평균클릭수_PC',
           'monthlyAvePcCtr': '월평균클릭률_PC', 'monthlyMobileQcCnt': '월간검색수_모바일',
           'monthlyPcQcCnt': '월간검색수_PC', 'plAvgDepth': '월평균노출광고수',
           'relKeyword': '연관키워드'}, axis=1, inplace=True)
df.head()

df = df[['연관키워드', '월간검색수_PC', '월간검색수_모바일', '월평균클릭수_PC', '월평균클릭수_모바일',
        '월평균클릭률_PC', '월평균클릭률_모바일', '경쟁정도', '월평균노출광고수']]
df.head()

print(df)
