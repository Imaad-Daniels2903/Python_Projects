import requests


MAGIC_EQUATION = [2, 9, 0, 3, 1, 0, 0, 1]  # this can be any 8 digit value


def div_split(ran_num):
    div_num = 1000
    list_range = 0
    if (ran_num % div_num) != 0:
        list_range = (ran_num // div_num) + 1
        div_spread = [0] * list_range
        for x in range(list_range):
            if x == (list_range - 1):
                div_spread[x] = ran_num % div_num
            else:
                div_spread[x] = div_num
    else:
        list_range = (ran_num // div_num)
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
PI_arr = [0] * 10

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
    PI_array = Get_PI(get_digits(Max * 8))

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
        ord_val += PI_array[cnt]
        binary = Binary(ord_val)

        for i in range(len(binary)):
            binary_list.append(int(binary[i]) + PI_array[i])

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
