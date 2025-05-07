import requests

# 1.拿到contId
# 2.拿到videoStatus返回的json拿到srCURL
# 3.srcURL里面的内容进行修整
# 4.下载视频


# 1.拿到contId
url = 'https://www.pearvideo.com/video_1796875'
contId = url.split("_")[1]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    # 防盗链:溯源，是当前请求的上一级
    , 'referer': url
}
videoStatus = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.39051081176800473'
resp = requests.get(videoStatus, headers=headers)
print(resp.json())
srcUrl = resp.json()['videoInfo']['videos']['srcUrl']
systemTime = resp.json()['systemTime']
srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')
print(srcUrl)

# https://video.pearvideo.com/mp4/short/20241028/cont-1796875-16039438-hd.mp4
# https://video.pearvideo.com/mp4/short/20241028/1731640896281-16039438-hd.mp4

# 下载视频,操作和下载图片是一样的
with open("video01.mp4", mode='wb') as f:
    f.write(requests.get(srcUrl).content)
