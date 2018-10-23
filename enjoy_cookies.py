import requests

if __name__ == '__main__':
    payload = {'username': 'Morvan', 'password': 'password'}
    r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())

    # {'username': 'Morvan', 'loggedin': '1'}

    r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
    print(r.text)

    # Hey Morvan! Looks like you're still logged into the site!