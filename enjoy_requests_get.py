# coding: utf-8
import webbrowser

import requests

if __name__ == '__main__':
    params = {"wd": u"莫烦python"}
    r = requests.get('https://www.baidu.com/s', params)
    
    webbrowser.open(r.url)

    pass
