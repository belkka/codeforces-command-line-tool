#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


BASE_URL = 'http://codeforces.com/api/'


def method(name):
    def cf_api_method(**kwargs):
        headers = { 'Accept-Language': 'ru,en;q=0.9' }

        r = requests.get(BASE_URL + name, params=kwargs, headers=headers)
        r.raise_for_status()

        cfreply = r.json()
        if cfreply['status'] == 'OK':
            return cfreply['result']
        else:
            assert cfreply['status'] == 'FAILED'
            raise Exception(cfreply['comment'])
    return cf_api_method


contest_standings = method('contest.standings')
user_info = method('user.info')
