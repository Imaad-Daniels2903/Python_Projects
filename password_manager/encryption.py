

def alphabetical_order(order_list):
    alphabetical_order_list = []
    new_alphabetical_order_list = []
    new_order_list = sorted(order_list)
    temp_list = []
    cnt = 0
    for i in range(len(order_list)):
        if cnt >= 1:
            if new_order_list[i] == new_order_list[i- 1]:
                alphabetical_order_list.append(chr((cnt - 1) + 65))
            else:
                alphabetical_order_list.append(chr(cnt + 65))
                cnt += 1
        else:
            alphabetical_order_list.append(chr(cnt + 65))
            cnt += 1

    for i in range(len(order_list)):
        for z in range(len(new_order_list)):
            if order_list[i] == new_order_list[z]:
                new_alphabetical_order_list.append(alphabetical_order_list[z])
                break

    for i in range(len(new_alphabetical_order_list)):
        temp_list.append(ord(new_alphabetical_order_list[i]))
        new_alphabetical_order_list[i] = chr(temp_list[i] + (ord(new_alphabetical_order_list[i]) - 64))

    return new_alphabetical_order_list

def encrypt_text(input_text):
    vowel_subs = [['a', '*'], ['e', '&'], ['i', '@'], ['o', '?'], ['u', '$']]
    input_list = []
    ascii_list = []
    vowel_sub_pos = []

    for i in range(len(input_text)):
        input_list.append(input_text[i])
        ascii_list.append(ord(input_list[i]))
        for vowel_loop in range(len(vowel_subs)):
            if input_list[i] == vowel_subs[vowel_loop][0]:
                vowel_sub_pos.append([i, vowel_subs[vowel_loop][1]])
    encrypt_list = alphabetical_order(ascii_list)

    for i in range(len(encrypt_list)):
        for z in range(len(vowel_sub_pos)):
            if vowel_sub_pos[z][0] == i:
                encrypt_list[i] = vowel_sub_pos[z][1]

    return ''.join(encrypt_list)



