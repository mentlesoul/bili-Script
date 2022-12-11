import requests
import re
import time

start = time.time()
mid = 指定用户主页uid
likelink = 'https://api.bilibili.com/x/web-interface/archive/like'
headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.41",
    'cookie': 放你自己的cookie,
}
formdata = {'like': '1', 'csrf': re.findall('bili_jct=(.*?);', headers['cookie'])[0]}


def Likes(url):
    res = requests.get(url).text
    formdata['aid'] = re.findall('"aid":(.*?),', res)[0]
    try:
        statue = requests.post(likelink, data=formdata, headers=headers)
        if statue.json()['message'] == '已赞过':
            print("av%s已赞过" % (formdata['aid']))
        return 1
    except:
        print('there has some trouble')


def main():
    pg = 1
    num = 0
    while True:
        base_url = 'https://api.bilibili.com/x/space/arc/search?mid={}&pn={}&ps=20&index=1'.format(mid, pg)
        pg += 1
        res = requests.get(base_url, headers=headers).json()
        bvid = res['data']['list']['vlist']
        if not bvid:
            break
        for i in bvid:
            bv = i['bvid']
            num += Likes("https://www.bilibili.com/video/" + bv)
    print("尝试点赞了%s次" % (num))
    end = time.time()
    print("运行时间：%s秒" % (end - start))


main()
