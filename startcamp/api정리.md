

# <u>기본주소</u>

* https://api.telegram.org/bot1818055641:AAELxGN8PaKPxMwlsjC8XAVMJDBdrDtEe9c

# 매서드

* https://api.telegram.org/bot1818055641:AAELxGN8PaKPxMwlsjC8XAVMJDBdrDtEe9c/getme

* https://api.telegram.org/bot1818055641:AAELxGN8PaKPxMwlsjC8XAVMJDBdrDtEe9c/getupdates

# 메세지보내기

* https://api.telegram.org/bot1818055641:AAELxGN8PaKPxMwlsjC8XAVMJDBdrDtEe9c/sendmessage?chat id=토큰=해윙



```python
#요청
import requests

#토큰저장
TOKEN = '토큰'
APP_URL = f'http://api.telegram.org/bot{TOKEN}' 

#url요청, 결과를 python 자료구조로 저장
update_url = f'{APP_URL}/getupdates'
response = requests.get(update_url).json()

#1. 사용자정보 가져오기
# /getupdates 요청보내서 #chat_id 해당하는 값을 저장
chat_id= response.get('result')[0].get('message').get('chat').get('id')


#2. 메세지 보내기
text= '해윙~'
send_message_url = f'{APP_URL}/sendmessage?chat_id={chat_id}&text={text}'

#3. 요청
requests.get(send_message_url)

```



## 날씨코드



```python
# 0. import!
# 항상 최상단에 작성을 해주세요.
import requests

# 1. URL에 파이썬으로 요청
url = 'https://www.metaweather.com/api/location/1132599'
response = requests.get(url)
# 2. JSON 형식을 파이썬 자료구조 변환 (.json())
result = response.json()
# 3. 원하는 값을 추출
# print(result['consolidated_weather'])
# print(type(result['consolidated_weather']))
# 4. 첫번째 데이터
day = result['consolidated_weather'][0]

print(f'''{day['applicable_date']} : {day["weather_state_name"]}
최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}''')

# 5. 무엇을 반복해야하는가?
# result['consolidated_weather']!!!
trans = {
    'Snow': '눈',
    'Sleet' : '진눈깨비',
    'Hail' : '우박',
    'Thunderstorm' : '뇌우',
    'Heavy Rain' : '폭우',
    'Light Rain' : '가벼운 비',
    'Showers' : '소나기',
    'Heavy Cloud' : '구름많음',
    'Light Cloud' : '구름조금',
    'Clear' : '맑은'
}
for day in result['consolidated_weather']:
    print(f'''{day['applicable_date']} : {trans[day["weather_state_name"]]}
최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}''')
```

