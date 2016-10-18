import hashlib, urllib.request, optparse
from termcolor import colored
import bs4

global_hash_code = None


def get_remote_md5_sum(url, max_file_size=100 * 1024 * 1024):
    global global_hash_code
    content = get_content(url)
    data = str.encode(content)
    hash_code = hashlib.md5()

    if len(data) > max_file_size:
        print('size is over')
        exit(1)

    hash_code.update(data)
    if global_hash_code is None:
        global_hash_code = hash_code
    elif not global_hash_code.hexdigest() == hash_code.hexdigest():
        print('content is changed')
        global_hash_code = hash_code
    return global_hash_code.hexdigest()


def get_content(url):
    r = urllib.request.Request(url)
    r.add_header('User-Agent', 'Mozilla/5.0')
    remote = urllib.request.urlopen(r)
    soup = bs4.BeautifulSoup(remote.read(), 'html.parser')
    h = soup.find('div', {'id': 'hc-container'})
    return str(h)


def loop_x_times(url):
    count = 0
    while count < 10:
        count += 1
        print(colored(get_remote_md5_sum(url), 'blue'))


if __name__ == '__main__':
    opt = optparse.OptionParser()
    opt.add_option('--url', '-u', default='http://www.google.com')
    options, args = opt.parse_args()
    if len(args) <= 0:
        loop_x_times(options.url)
    else:
        loop_x_times(args[0])

# get_content(r'http://www.adidas.com/us/nmd-shoes')
