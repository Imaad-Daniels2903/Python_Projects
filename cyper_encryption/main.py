from Tools.i18n.makelocalealias import pprint

import cypher, Encrypt
from Encrypt import encrypt_text

user_input = input('Enter text:')
# fully_encrypted_text = Encrypt.encrypt_text(cypher.cypher_text(user_input))
# print(fully_encrypted_text)
print(encrypt_text(user_input))