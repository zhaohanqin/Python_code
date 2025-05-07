from lxml import etree
import requests

# 拿到页面源代码
# 提取和解析数据

url = 'https://www.zbj.com/fw/?k=saas'
headers = {
    'cookie': '_uq=b87025eda36a4d4ebff951722b19d391; uniqid=d014c7irrnhb78; _suq=e0d09b77-b304-4fd4-beda-37aa61fe9a39; nsid=s%3AMnmAzJdtdy473LzuMAVvpU4X1f-ZPknF.x%2FwaCg%2FSMrIgjxYc2a4gePzaitPH179r%2Ffz4m3kxchU; local_city_path=changsha; local_city_name=%E9%95%BF%E6%B2%99; local_city_id=3645; unionJsonOcpc=eyJvdXRyZWZlcmVyIjoiaHR0cHM6Ly9jbi5iaW5nLmNvbS8iLCJwbWNvZGUiOiIxMzI4MDEzNjciLCJ1dG1fc291cmNlIjoic291Z291In0%3D; Hm_lvt_a360b5a82a7c884376730fbdb8f73be2=1730813735,1730884116; HMACCOUNT=5441D3469E862908; vidSended=1; oldvid=bb213c6e0feaccf8c2a1259736fddd2e; vid=2f840589d1642ce689c763dcff5eceb2; Hm_lpvt_a360b5a82a7c884376730fbdb8f73be2=1730894635; s_s_c=xhA3dh7QsA2lgP8ro4tGRySwnIERGWjvArJ%2B78u21sB2Ra%2FoVN%2FEIF2%2F4hLum5Hf2%2Bz3fLDkm1UlRWQNgcKUy1rUlXx07zIfXcJumRkWZzw%3D',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}
resp = requests.get(url, headers=headers)
# print(resp.text)


html = etree.HTML(resp.text)
# 拿到每个服务商的div
divs = html.xpath("/html/body/div[2]/div/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div")
for div in divs:  # 每个服务商的信息
    price = div.xpath('./div/div/div[2]/div[1]/span/text()')
    print(price)