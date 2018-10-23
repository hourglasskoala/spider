# coding: utf-8
import requests

if __name__ == '__main__':
    data = {'firstname': u'沙漏', 'lastname': u'考拉'}
    r = requests.post("http://pythonscraping.com/files/processing.php", data=data)
    print(r.text)
