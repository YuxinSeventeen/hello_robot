import requests
import os

WEBHOOK_KEY = os.environ.get("WECHAT_WEBHOOK_KEY")

url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={WEBHOOK_KEY}"

msg = {
    "msgtype": "text",
    "text": {
        "content": "测试中：今天是星期四，16:00定时发送此消息。大家下午好~"
    }
}

resp = requests.post(url, json=msg)
print(resp.text)
