#!/usr/bin/env python

import sys
import requests


def get_content(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    return None


def run():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "http://baidu.com"

    content = get_content(url)

    if content:
        print(content)
    else:
        print("Hello world!")
