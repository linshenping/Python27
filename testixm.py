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
        print '#########获取access_token用例执行############'
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

    # 获取参保人信息jiekou
    def test_get_insured_information(self):
        print '##########获取参保人信息用例执行############'
        #获取accsess_token
        date_token = {
            "funid": "N03.00.05.11",
            "data": {
            "app_type": "0",
            "appid": "xmggfw"
                    },
            "appid": "xmggfw"
                }
        r = requests.post(url=self.url, json=date_token)
        access_token = r.json()['data']['access_token']
        print 'access_token:{0}'.format(access_token)

        #请求参保人信息
        date = {
            "funid": "N06.00.01.02",
            "data": {
                "access_token": access_token,
                "uid": "350823199311161020"
            },
            "access_token": access_token
        }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')
        
        
        # 机构信息查询
    def test_institutional_information_inquiry(self):
        print '##########机构信息查询用例执行############'
        date = {
            "funid": "N07.03.00.21",
            "data": {
            "aab299": "210600"
            }
            }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 跨省异地备案列表查询(机构)
    def test_inter_provincial_record_mechanism_list(self):
        print '##########跨省异地备案列表查询（机构）用例执行############'
        date = {
            "funid": "N07.03.00.16",
            "data": {
            "social_credit_code": "91350200MA31GUTX75",
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


    # 跨省异地备案申请
    def test_inter_provincial_filing_application(self):
        print '########跨省异地备案申请用例执行############'
        date = {
            "funid": "N07.03.00.17",
            "data": {
            "uid":"350603199510110019",
            "record_type":"2",
            "record_city":"210600",
            "effect_date":"2019-08-05",
            "contact_person":"林小延",
            "contact_phone":"18650347652",
            "contact_addr":"快乐快乐",
            "hospitals":"丹东市公安医院",
            "medicals":"国大药房",
            "org_codes":"2106001000002",
            "apply_channel":"01"
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 2.4.1	跨省异地备案列表查询(个人)
    def test_inter_provincial_record_personal_list(self):
        print '##############跨省异地备案列表查询(个人)用例执行##############'
        date = {
            "funid": "N07.03.00.16",
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
        id = r.json()['data']['rows'][0]['id']
        print 'id是: {0}'.format(id)
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')


    # 跨省异地备案撤销
    def test_inter_provincial_filing_cancel(self):
        print '##########跨省异地备案撤销用例执行############'
        # 查询最新的id是多少
        date_id = {
            "funid": "N07.03.00.16",
            "data": {
                "uid": "350603199510110019",
                "page": "1",
                "rows": "10"
            }
        }
        r = requests.post(url=self.url, json=date_id)
        id = r.json()['data']['rows'][0]['id']
        print 'id是: {0}'.format(id)

        #  api请求
        date = {
            "funid": "N07.03.00.18",
            "data": {
            "id": id
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')


    # 跨省异地备案截止（数据目前没办法构造）
    def test_inter_provincial_filing_cutoff(self):
        print '##########跨省异地备案截止用例执行############'
        date = {
            "funid": "N07.03.00.19",
            "data": {
            "id": "194190"
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')


    # 跨省异地备案前置校验
    def test_inter_provincial_filing_check(self):
        print '##########跨省异地备案前置校验用例执行############'
        date = {
            "funid": "N07.03.00.20",
            "data": {
            "uid": "350603199510110019"
			}
		}
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 模糊查找本单位人员姓名jiekou
    def test_fuzzy_search(self):
        print '##########模糊查找本单位人员姓名用例执行############'
        date = {
        "funid": "N07.03.00.23",
        "data": {
            "social_credit_code": "91350200MA31GUTX75",
            "name": "王"
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
    unittest.main()


