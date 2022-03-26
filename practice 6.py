# practice 6 - 크롤러 만들기 
# 2021년 영화 역대 관객순위 상위 5개 이미지 다운로드

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&q=2021%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
images =  soup.find_all("img", attrs={"class": "thumb_img"})

for idx, image in enumerate(images):
    #print(image["src"])
    img_url = image["src"]
    if img_url.startswith("//"):
        img_url = "https:" + img_url

    #print(img_url)
    # 해당 사이트에 접속해서 이미지를 가지고 오기 위해 다시 한 번 requests로 접속함
    img_res = requests.get(img_url)
    img_res.raise_for_status()

    # image 저장, wb는 이미지가 텍스트가 아니라 바이너리라서 b를 붙여줌
    print("dd")
    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(img_res.content)
        print("ssss")
    
    # 상위 5개 이미지 다운로드
    if idx >= 4:
        break;
