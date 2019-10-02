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


#crop face 

전체 폴더명 순서대로 번호 붙이기
ex)download/AOA설현 -> 1
new=0;for i in *;do ext="${i#*.}";mv "$i" "$new";((new++));done

폴더를 돌면서 얼굴 잘라진 crop 폴더와 ,face detect되지 않는 원본 사진은 reject폴더로
new=0;for new in {0..103};do autocrop -i  ./download/"$new"  -o crop/"$new"  -r reject/"$new"  -w 512 -H 512 --facePercent 90;((new++));done

