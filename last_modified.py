from urllib.request import urlopen
import urllib.request, http.cookiejar
import time

req = urllib.request.Request(r'https://www.stackoverflow.com/', headers={'User-Agent': 'Mozilla/5.0'})
cj = http.cookiejar.CookieJar()
# conn = urllib.request.build_opener(urllib.request.) urlopen(req)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
conn = opener.open(req)
last_modified = conn.headers['Last-Modified']
conn.close()

print("Last Modified time: %s" % last_modified)


def request_ten_time():
    global last_modified, req, cj
    req.add_header('If-Modified-Since', last_modified)
    try:
        con = opener.open(req)
        if not con['Last-Modified'] == last_modified:
            temp = last_modified
            last_modified = con['Last-Modified']
            print("Last Modified date changed from %s to %s" % (temp, last_modified))
        con.close()
    except urllib.request.HTTPError as err:
        if err.code == 304:
            print("Last Modified date is not changed, the date is still: %s" % last_modified)
        elif err.code == 301:
            print(format(err))
        else:
            raise
    finally:
        cj.clear()


count = 0
while count < 100:
    count += 1
    time.sleep(1)
    request_ten_time()
    print("count: %s" % count)


if __name__ == '__main__':
    serve