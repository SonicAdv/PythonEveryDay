# 这个脚本用来构造setting多个接口的请求
#/usr/env/python

from storage_base import *
import hashlib
import urllib2

def calculate_sign(app_id):
    conn = get_adn_mongo_connection()
    db = conn.new_adn
    content = db.app.find_one({'appId':app_id}, {'publisher.apiKey':1, '_id':0})
    if content == None:
        return None
    m2 = hashlib.md5()
    m2.update(str(app_id) + content['publisher']['apiKey'])
    return m2.hexdigest()

def query(url):
    print url
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    obj = json.loads(res)
    return json.dumps(obj, indent = 4)

def setting(app_id, unit_id = 0):
    sign = calculate_sign(app_id)
    if sign == None:
        print 'unit_id %d not exist!' % app_id
        return None
    url = "http://setting.rayjump.com/setting?app_id=%d&sign=%s" % (app_id, sign)
    if unit_id != 0:
        url += '&unit_ids=[%d]' % unit_id
    return query(url)

def appwallsetting(app_id, unit_id = 0):
    sign = calculate_sign(app_id)
    print sign
    if sign == None:
        print 'app_id %d not exist!' % app_id
        return None
    url = "http://setting.rayjump.com/appwall/setting?app_id=%d&sign=%s" % (app_id, sign)
    if unitId != 0:
        url += '&unit_id=%d' % unit_id
    return query(url)

def rewardsetting(app_id, unit_id = 0):
    sign = calculate_sign(app_id)
    print sign
    if sign == None:
        print 'app_id %d not exist!' % app_id
        return None
    url = "http://setting.rayjump.com/rewardsetting?app_id=%d&sign=%s" % (app_id, sign)
    if unitId != 0:
        url += '&unit_ids=[%d]' % unit_id
    return query(url)

def jssetting(app_id, unit_id):
    sign = calculate_sign(app_id)
    if sign == None:
        print 'unit_id %d not exist!' % app_id
        return None
    url = "http://setting.rayjump.com/jssetting?app_id=%d&sign=%s&unit_id=%s" % (app_id, sign, str(unit_id))
    return query(url)

def main():
    print setting(25605)
    return 0
    print setting(32544, 11092)
    print appwallsetting(18988, 23)
    print appwallsetting(18988)
    print rewardsetting(32544, 11092)
    print rewardsetting(32544)
    print jssetting(32544, 11092)

if __name__ == "__main__":
    main()
