from yiqihaha/auto-build-test

add . /app
WORKDIR /app/myproject

run scrapy crawl test -o test.json

cmd ["cat","/app/myproject/test.json"]