import json
import os

import requests


def get_wechat_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {'corpid': os.environ.get('WECHAT_CORPID', ''),
              'corpsecret': os.environ.get('WECHAT_CORPSECRET', ''), }
    req = requests.post(url, params=values)
    data = json.loads(req.text)
    return data.get("access_token")


def notice_wechat(message):
    url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + get_wechat_token()
    values = '''{"touser": "@all",
      "msgtype":"text",
      "agentid":"1000002",
      "text":{
        "content": "%s"
      },
      "safe":"0"
      }''' % (str(message))
    response = requests.post(url, values)
    return response


if __name__ == '__main__':
    notice_wechat('Sample Content')
