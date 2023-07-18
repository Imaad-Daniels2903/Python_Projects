import requests

FIRST_THOUSAND_OF_PI = [1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0,
                        2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8, 2, 0, 9, 7, 4, 9, 4, 4, 5, 9, 2, 3,
                        0, 7, 8, 1, 6, 4, 0, 6, 2, 8, 6, 2, 0, 8, 9, 9, 8, 6, 2, 8, 0, 3, 4, 8, 2, 5, 3, 4, 2, 1, 1, 7,
                        0, 6, 7, 9, 8, 2, 1, 4, 8, 0, 8, 6, 5, 1, 3, 2, 8, 2, 3, 0, 6, 6, 4, 7, 0, 9, 3, 8, 4, 4, 6, 0,
                        9, 5, 5, 0, 5, 8, 2, 2, 3, 1, 7, 2, 5, 3, 5, 9, 4, 0, 8, 1, 2, 8, 4, 8, 1, 1, 1, 7, 4, 5, 0, 2,
                        8, 4, 1, 0, 2, 7, 0, 1, 9, 3, 8, 5, 2, 1, 1, 0, 5, 5, 5, 9, 6, 4, 4, 6, 2, 2, 9, 4, 8, 9, 5, 4,
                        9, 3, 0, 3, 8, 1, 9, 6, 4, 4, 2, 8, 8, 1, 0, 9, 7, 5, 6, 6, 5, 9, 3, 3, 4, 4, 6, 1, 2, 8, 4, 7,
                        5, 6, 4, 8, 2, 3, 3, 7, 8, 6, 7, 8, 3, 1, 6, 5, 2, 7, 1, 2, 0, 1, 9, 0, 9, 1, 4, 5, 6, 4, 8, 5,
                        6, 6, 9, 2, 3, 4, 6, 0, 3, 4, 8, 6, 1, 0, 4, 5, 4, 3, 2, 6, 6, 4, 8, 2, 1, 3, 3, 9, 3, 6, 0, 7,
                        2, 6, 0, 2, 4, 9, 1, 4, 1, 2, 7, 3, 7, 2, 4, 5, 8, 7, 0, 0, 6, 6, 0, 6, 3, 1, 5, 5, 8, 8, 1, 7,
                        4, 8, 8, 1, 5, 2, 0, 9, 2, 0, 9, 6, 2, 8, 2, 9, 2, 5, 4, 0, 9, 1, 7, 1, 5, 3, 6, 4, 3, 6, 7, 8,
                        9, 2, 5, 9, 0, 3, 6, 0, 0, 1, 1, 3, 3, 0, 5, 3, 0, 5, 4, 8, 8, 2, 0, 4, 6, 6, 5, 2, 1, 3, 8, 4,
                        1, 4, 6, 9, 5, 1, 9, 4, 1, 5, 1, 1, 6, 0, 9, 4, 3, 3, 0, 5, 7, 2, 7, 0, 3, 6, 5, 7, 5, 9, 5, 9,
                        1, 9, 5, 3, 0, 9, 2, 1, 8, 6, 1, 1, 7, 3, 8, 1, 9, 3, 2, 6, 1, 1, 7, 9, 3, 1, 0, 5, 1, 1, 8, 5,
                        4, 8, 0, 7, 4, 4, 6, 2, 3, 7, 9, 9, 6, 2, 7, 4, 9, 5, 6, 7, 3, 5, 1, 8, 8, 5, 7, 5, 2, 7, 2, 4,
                        8, 9, 1, 2, 2, 7, 9, 3, 8, 1, 8, 3, 0, 1, 1, 9, 4, 9, 1, 2, 9, 8, 3, 3, 6, 7, 3, 3, 6, 2, 4, 4,
                        0, 6, 5, 6, 6, 4, 3, 0, 8, 6, 0, 2, 1, 3, 9, 4, 9, 4, 6, 3, 9, 5, 2, 2, 4, 7, 3, 7, 1, 9, 0, 7,
                        0, 2, 1, 7, 9, 8, 6, 0, 9, 4, 3, 7, 0, 2, 7, 7, 0, 5, 3, 9, 2, 1, 7, 1, 7, 6, 2, 9, 3, 1, 7, 6,
                        7, 5, 2, 3, 8, 4, 6, 7, 4, 8, 1, 8, 4, 6, 7, 6, 6, 9, 4, 0, 5, 1, 3, 2, 0, 0, 0, 5, 6, 8, 1, 2,
                        7, 1, 4, 5, 2, 6, 3, 5, 6, 0, 8, 2, 7, 7, 8, 5, 7, 7, 1, 3, 4, 2, 7, 5, 7, 7, 8, 9, 6, 0, 9, 1,
                        7, 3, 6, 3, 7, 1, 7, 8, 7, 2, 1, 4, 6, 8, 4, 4, 0, 9, 0, 1, 2, 2, 4, 9, 5, 3, 4, 3, 0, 1, 4, 6,
                        5, 4, 9, 5, 8, 5, 3, 7, 1, 0, 5, 0, 7, 9, 2, 2, 7, 9, 6, 8, 9, 2, 5, 8, 9, 2, 3, 5, 4, 2, 0, 1,
                        9, 9, 5, 6, 1, 1, 2, 1, 2, 9, 0, 2, 1, 9, 6, 0, 8, 6, 4, 0, 3, 4, 4, 1, 8, 1, 5, 9, 8, 1, 3, 6,
                        2, 9, 7, 7, 4, 7, 7, 1, 3, 0, 9, 9, 6, 0, 5, 1, 8, 7, 0, 7, 2, 1, 1, 3, 4, 9, 9, 9, 9, 9, 9, 8,
                        3, 7, 2, 9, 7, 8, 0, 4, 9, 9, 5, 1, 0, 5, 9, 7, 3, 1, 7, 3, 2, 8, 1, 6, 0, 9, 6, 3, 1, 8, 5, 9,
                        5, 0, 2, 4, 4, 5, 9, 4, 5, 5, 3, 4, 6, 9, 0, 8, 3, 0, 2, 6, 4, 2, 5, 2, 2, 3, 0, 8, 2, 5, 3, 3,
                        4, 4, 6, 8, 5, 0, 3, 5, 2, 6, 1, 9, 3, 1, 1, 8, 8, 1, 7, 1, 0, 1, 0, 0, 0, 3, 1, 3, 7, 8, 3, 8,
                        7, 5, 2, 8, 8, 6, 5, 8, 7, 5, 3, 3, 2, 0, 8, 3, 8, 1, 4, 2, 0, 6, 1, 7, 1, 7, 7, 6, 6, 9, 1, 4,
                        7, 3, 0, 3, 5, 9, 8, 2, 5, 3, 4, 9, 0, 4, 2, 8, 7, 5, 5, 4, 6, 8, 7, 3, 1, 1, 5, 9, 5, 6, 2, 8,
                        6, 3, 8, 8, 2, 3, 5, 3, 7, 8, 7, 5, 9, 3, 7, 5, 1, 9, 5, 7, 7, 8, 1, 8, 5, 7, 7, 8, 0, 5, 3, 2,
                        1, 7, 1, 2, 2, 6, 8, 0, 6, 6, 1, 3, 0, 0, 1, 9, 2, 7, 8, 7, 6, 6, 1, 1, 1, 9, 5, 9, 0, 9, 2, 1,
                        6, 4, 2, 0, 1, 9, 8]
MAGIC_EQUATION = [2, 9, 0, 3, 1, 0, 0, 1] # this can be anny 10 digit value


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

def Get_PI(PI_string):
    Pi_array = []
    for x in range(len(PI_string)):
        Pi_array.append(int(PI_string[x]))

    return Pi_array
def subtract(in_val, inlst):
    empty_list = []
    leng = len(inlst)
    sub_val = 0
    i = 0
    l = 0
    flag = False
    while i != leng:
        sub_val = in_val - inlst[i]
        empty_list.insert(i, sub_val)
        i += 1
    while not flag:
        if empty_list[l] < 0:
            l += 1
        else:
            flag = True
            return l

def Binary(u_input):
    # basic initialisation
    ate_list = [128, 64, 32, 16, 8, 4, 2, 1]
    two_byte = [32768, 16284, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    # user_val = int(input("enter value" + "\n"))
    display_box = []
    dummy_list = []
    pos_box = []
    if u_input > 255:
        dummy_list = two_byte
    else:
        dummy_list = ate_list
    coder_val = u_input
    leng = len(dummy_list)
    bober_val = 0
    i = 0
    l = 0
    bin_val = ""

    # filling pos_box with positions of used numbers from ate_bits list
    while coder_val != 0:
        bober_val = coder_val
        coder_val = coder_val - dummy_list[subtract(coder_val, dummy_list)]
        pos_box.insert(i, subtract(bober_val, dummy_list))
        i += 1

    # filling the string with the converted value
    for l in range(len(dummy_list)):
        if l in pos_box:
            bin_val += str(1)
        else:
            bin_val += str(0)

    # displaying result
    return bin_val

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
    cnt = 0
    binary = ""
    binary_list = []
    Magic_equ = []
    Final = []
    encrypt_list = []
    Final_text = ""
    user_input = input("enter text: ")
    Max = len(user_input)
    PI_array = Get_PI(get_digits(Max))

    while cnt != Max:
        ord_val = 0
        i = 0
        k = 0
        l = 0
        binary = ""
        Final_text = ""
        binary_list = []
        Magic_equ = []
        Final = []
        ord_val = ord(user_input[cnt])
        ord_val += FIRST_THOUSAND_OF_PI[cnt]
        binary = Binary(ord_val)

        for i in range(len(binary)):
            binary_list.append(int(binary[i]) + FIRST_THOUSAND_OF_PI[i])

        for k in range(len(binary_list)):
            Magic_equ.append(binary_list[k] + MAGIC_EQUATION[k])

        for l in range(len(Magic_equ)):
            Final.append(chr(Magic_equ[l] + 64))

        Final_text = Final_text.join(Final)
        encrypt_list.append(Final_text)
        cnt += 1
        display = ""
    print(display.join(encrypt_list))
    print(PI_array)