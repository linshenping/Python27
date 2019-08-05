# -*- coding: utf-8 -*-
import requests
import urllib3
import json
import unittest
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class GetIxmApiTest(unittest.TestCase):
    def setUp(self):
        self.url = "https://ylbz.ixm.gov.cn/xmyb/api/gafe/rest"

    # 获取access_token
    def test_get_access_token(self):
        # 入参
        date = {
            "funid": "N03.00.05.11",
            "data": {
                "app_type": "0",
                "appid": "xmggfw"
            },
             "appid": "xmggfw"
        }
        r = requests.post(url=self.url, json=date)
        print r.text
        datas = json.loads(r.text.encode('utf-8')).get('data')
        print('datas{0}:'.format(datas))
        access_token = datas.get('access_token')
        print 'access_token:{0}'.format(access_token)
        flags = json.loads(r.text).get('flag')
        print 'flags:{0}'.format(flags)
        expires_time = datas.get('expires_in')
        print 'expires_time:{0}'.format(expires_time)
        refresh_token = datas.get('refresh_token')
        print 'refresh_token:{0}'.format(refresh_token)
        self.assertEqual(flags, u'1')

    # 获取参保人信息
    def test_get_insured_information(self):
        date = {
            "funid": "N06.00.01.02",
            "data": {
                "access_token": "fe038b3f423db15d3addb2cc368de479",
                "uid": "350823199311161020"
            },
            "access_token": "fe038b3f423db15d3addb2cc368de479"
        }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 2.4.1	跨省异地备案列表
    def test_inter_provincial_record_list(self):
        date = {
            "funid": "N07.03.00.01",
            "data": {
            "uid": "350603199510110019",
            "page": "1",
            "rows": "10"
                }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')



if __name__ == '__main__':
    unittest.main(verbosity=2)


