from builtins import print
import requests

def div_split(ran_num):
    div_num = 1000
    list_range = 0
    if (ran_num % div_num) != 0:
        list_range = (ran_num//div_num) + 1
        div_spread = [0] * list_range
        for x in range(list_range):
            if x == (list_range - 1):
                div_spread[x] = ran_num % div_num
            else:
                div_spread[x] = div_num
    else:
        list_range = (ran_num//div_num)
        div_spread = [0] * list_range
        for x in range(list_range):
                div_spread[x] = div_num

    return div_spread

def get_digits(in_num):
    start_p = 0
    num_div = div_split(in_num)
    num_str = ''

    for x in range(len(num_div)):
        API = 'https://api.pi.delivery/v1/pi?start=' + str(start_p) + '&numberOfDigits=' + str(num_div[x]) + '&radix=10'
        response = requests.get(API)
        num_str += str(response.json()['content'])
        start_p += 1000

    return num_str

API_url = 'https://api.pi.delivery/v1/pi?start=0&numberOfDigits=1000&radix=10'
good_URL = True
response = ''
PI_arr = [0]*10

try:
    response = requests.get(API_url)
except:
        print('URL PROBLEM!!!')
        good_URL = False

if good_URL:
    # print(response.json()['content'])
    digits = get_digits(int(input('enter amount of digits:')))
    for x in range(len(digits)):
        PI_arr[int(digits[x])] += 1
        
    print(digits)
    print(len(digits))
    print(PI_arr)
    print((sum(PI_arr))/(len(PI_arr)))
    print(sum(PI_arr))

