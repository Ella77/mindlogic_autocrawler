# AutoCrawler
Google, Naver multiprocess image crawler (High Quality & Speed & Customizable)

![](docs/animation.gif)

# How to use

1. Install Chrome

2. pip install -r requirements.txt

3. Write search keywords in keywords.txt

4. **Run "main.py"**

5. Files will be downloaded to specific directory. 'download_path'in train.py

chrome, chromedriver version compatibility와 version별 error 

# Arguments
usage:
```
python3 main.py [--skip true] [--threads 4] [--google true] [--naver true] [--full false] [--face false]
```

```
--skip true        Skips keyword if downloaded directory already exists. This is needed when re-downloading.

--threads 4        Number of threads to download.

--google true      Download from google.com (boolean)

--naver true       Download from naver.com (boolean)

--full false       Download full resolution image instead of thumbnails (slow)

--face false       Face search mode
```


# Full Resolution Mode

You can download full resolution image of JPG, GIF, PNG files by specifying --full true

![](docs/full.gif)



# Data Imbalance Detection

Detects data imblance based on number of files.

When crawling ends, the message show you what directory has under 50% of average files.

I recommend you to remove those directories and re-download.


# Remote crawling through SSH on your server

```
sudo apt-get install xvfb <- This is virtual display

sudo apt-get install screen <- This will allow you to close SSH terminal while running.

screen -S s1

Xvfb :99 -ac & DISPLAY=:99 python3 main.py -threads 4 --google true --naver true --full true --face true
```

keywords.txt( 검색어 목록)과 output사진들이 다운로드될 download_path수정 필요

# Customize

You can make your own crawler by changing collect_links.py


# crop face 

전체 폴더명 순서대로 번호 붙이기
ex)download/AOA설현 -> 1
```
new=0;for i in *;do ext="${i#*.}";mv "$i" "$new";((new++));done
```
폴더를 돌면서 얼굴 잘라진 crop 폴더와 ,face detect되지 않는 원본 사진은 reject폴더로
```
new=0;for new in {0..103};do autocrop -i  ./download/"$new"  -o crop/"$new"  -r reject/"$new"  -w 512 -H 512 --facePercent 90;((new++));done
```
디렉토리 별로 분리된 파일들을 디렉토리명을 파일명으로 넣어 합치기
ex) 0/naver0001.jpg -> 0_naver0001.jpg
```
for new in {0..99};do for i in /hdd/celeb-images-crawled/face90/girl_crop/"$new"/*;do cp ”$i" ~/girl/"$new"_"$(basename "$i")";done;done
```

# 구글 이미지 크롤링 안되는 오류 해결

# chrome download

```sudo dpkg -i google-chrome-stable_current_amd64.deb```
dependency 오류시 sudo apt install -f 

when update needed, install chrome browser
```
$ sudo apt-get install libxss1 libgconf2-4 libappindicator1 libindicator7

$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 

$ sudo dpkg -i google-chrome-stable_current_amd64.deb
```

# chromedriver
no permisson -> ```chmod +x chromedriver/chromedriver_linux```
DevActivePorts error -> 코드내 headless 등 chrome option으로 해결됨
