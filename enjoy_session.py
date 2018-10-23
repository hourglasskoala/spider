import requests

if __name__ == '__main__':
    session = requests.Session()
    payload = {'username': 'Morvan', 'password': 'password'}
    r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
    print(r.cookies.get_dict())

    # {'username': 'Morvan', 'loggedin': '1'}

    r = session.get("http://pythonscraping.com/pages/cookies/profile.php")
    print(r.text)

    # Hey Morvan! Looks like you're still logged into the site!
