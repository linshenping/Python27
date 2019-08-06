# -*- coding: utf-8 -*-
import requests
import urllib3
import json
import unittest
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class GetIxmApiCrossProvinceTest(unittest.TestCase):

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

class GetIxmApiFixOrganizationTest(unittest.TestCase):

    def setUp(self):
            self.url = "https://ylbz.ixm.gov.cn/xmyb/api/gafe/rest"

    # 查询定点机构信息
    def test_query_fixed_point_organization_informationh(self):
        print '##########查询定点机构信息用例执行############'
        date = {
        "funid": "N07.07.00.01",
        "data": {
            "social_credit_code": "913502030511743851",
            "batch": ""
                }
            }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 定点机构信息新增
    def test_query_fixed_point_organization_new(self):
        print '##########定点机构信息新增用例执行############'
        date = {
            "funid": "N07.07.00.02",
            "data": {
                "apply_type": "01",
                "org_id": "*",
                "org_name": "TEST-linsp厦门最美信息科技有限公司",
                "network_area": "350203",
                "network_addr": "厦门市思明区海翼大厦厦禾路666",
                "key_project": "0",
                "key_project_file_no": "",
                "key_project_file_name": "",
                "contacts": "linsp-test",
                "contacts_certificate_type": "10",
                "contacts_certificate_no": "1234567890",
                "contacts_phone": "22222222222",
                "org_grade": "9",
                "org_type": "51",
                "ownership": "0",
                "operate_nature": "01",
                "license_key": "222222",
                "license_key_begin_date": "20190318",
                "certificate_no": "334343",
                "certificate_no_begin_date": "20190322",
                "social_credit_code": "913502030511743851",
                "business_license": "*",
                "is_org": "0",
                "one_apply_date": "",
                "one_apply_addr": "",
                "second_apply_date": "",
                "second_apply_adddr": "",
                "legal_person": "1",
                "legal_person_certificate_type": "10",
                "legal_person_certificate_no": "2222",
                "legal_person_phone": "23232323",
                "area": "100",
                "actual_area": "100",
                "building_begin_date": "201901",
                "building_end_date": "201907",
                "range": "厦门禹州大学城",
                "main_range": "口腔",
                "bed_num": "2",
                "is_punish": "0",
                "punish_office": "",
                "punish_date": "",
                "is_accident": "0",
                "doctor_num": "5",
                "senior_num": "1",
                "intermediate_num": "2",
                "technician_num": "1",
                "charge_num": "1",
                "apply_channel": "02",
                "street": "厦禾路666",
                "manage_begin_date": "20190128",
                "longitude": "118.23122",
                "latitude": "24.64738"

                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 定点机构信息修改
    def test_query_fixed_point_organization_update(self):
        print '##########定点机构信息修改用例执行############'
        # 查询获取serial_no和batch参数
        date_serial = {
            "funid": "N07.07.00.01",
            "data": {
                "social_credit_code": "913502030511743851",
                "batch": ""
            }
        }
        r = requests.post(url=self.url, json=date_serial)
        serial_no = r.json()['data'][0]['serial_no']
        print ('serial_no: {0}').format(serial_no)
        batch = r.json()['data'][0]['batch']
        print ('serial_no: {0}').format(batch)
        # api请求
        date = {
            "funid": "N07.07.00.03",
            "data": {
                "serial_no": serial_no,
                "batch": batch,
                "apply_type": "01",
                "org_id": "*",
                "org_name": "TEST-厦门最美信息科技有限公司",
                "network_area": "350203",
                "network_addr": "厦门市思明区海翼大厦厦禾路666",
                "key_project": "0",
                "key_project_file_no": "",
                "key_project_file_name": "",
                "contacts": "linsp-test",
                "contacts_certificate_type": "10",
                "contacts_certificate_no": "1234567890",
                "contacts_phone": "22222222222",
                "org_grade": "9",
                "org_type": "51",
                "ownership": "0",
                "operate_nature": "01",
                "license_key": "222222",
                "license_key_begin_date": "20190318",
                "certificate_no": "334343",
                "certificate_no_begin_date": "20190322",
                "social_credit_code": "913502030511743851",
                "business_license": "*",
                "is_org": "0",
                "one_apply_date": "",
                "one_apply_addr": "",
                "second_apply_date": "",
                "second_apply_adddr": "",
                "legal_person": "1",
                "legal_person_certificate_type": "10",
                "legal_person_certificate_no": "2222",
                "legal_person_phone": "23232323",
                "area": "100",
                "actual_area": "100",
                "building_begin_date": "201901",
                "building_end_date": "201907",
                "range": "厦门禹州大学城",
                "main_range": "口腔",
                "bed_num": "2",
                "is_punish": "0",
                "punish_office": "",
                "punish_date": "",
                "is_accident": "0",
                "doctor_num": "5",
                "senior_num": "1",
                "intermediate_num": "2",
                "technician_num": "1",
                "charge_num": "1",
                "apply_channel": "02",
                "street": "厦禾路666",
                "manage_begin_date": "20190128",
                "longitude": "118.23122",
                "latitude": "24.64738"

                    }
                }

        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 机构定点申请数据撤销
    def test_query_fixed_point_organization_cancle(self):
        print '##########机构定点申请数据撤销用例执行############'
        # 查询获取serial_no参数
        date_serial = {
            "funid": "N07.07.00.01",
            "data": {
                "social_credit_code": "913502030511743851",
                "batch": ""
            }
        }
        r = requests.post(url=self.url, json=date_serial)
        serial_no = r.json()['data'][0]['serial_no']
        print ('serial_no: {0}').format(serial_no)
        # api请求
        date = {
            "funid": "N07.07.00.04",
            "data": {
                "serial_no": serial_no
                    }
                }
        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 机构定点申请医师信息维护
    def test_query_fixed_point_doctor_information_add(self):
        print '##########机构定点申请医师信息维护(新增)用例执行############'
        # 查询获取serial_no参数
        date_serial = {
            "funid": "N07.07.00.01",
            "data": {
                "social_credit_code": "913502030511743851",
                "batch": ""
            }
        }
        r = requests.post(url=self.url, json=date_serial)
        serial_no = r.json()['data'][0]['serial_no']
        print ('serial_no: {0}').format(serial_no)
        # api请求
        date = {
            "funid": "N07.07.00.05",
            "data": {
                "serial_no": serial_no,
                "type": "1",
                "doctor_list": {
                    "biz_serial_no": "",
                    "people_type": "01",
                    "certificate_grade": "01",
                    "name": "萍萍",
                    "certificate_type": "10",
                    "certificate_no": "123454545",
                    "vocational_qc_no": "7787788",
                    "technical_qc_no": "2222222",
                    "title_certificate_no": "44444444",
                    "title_certificate_authorities": "厦门",
                    "licensed_pharmacist_qc_no": ""
                                }
                    }
                }

        r = requests.post(url=self.url, json=date)
        print r.text
        cause = json.loads(r.text).get('cause')
        print('cause: {0}'.format(cause))
        flags = json.loads(r.text).get('flag')
        print 'flags: {0}'.format(flags)
        self.assertEqual(flags, u'1')

    # 机构定点申请医师信息查询
    def test_query_fixed_point_doctor_information(self):
        print '##########机构定点申请医师信息查询用例执行############'
        # 查询获取serial_no参数
        date_serial = {
            "funid": "N07.07.00.01",
            "data": {
                "social_credit_code": "913502030511743851",
                "batch": ""
            }
        }
        r = requests.post(url=self.url, json=date_serial)
        serial_no = r.json()['data'][0]['serial_no']
        print ('serial_no: {0}').format(serial_no)
        # api请求
        date = {
            "funid": "N07.07.00.06",
            "data": {
                "serial_no": serial_no,
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
    unittest.main()


