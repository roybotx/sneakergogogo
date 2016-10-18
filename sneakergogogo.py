import requests
from bs4 import BeautifulSoup
import sqlite3 as lite
import sys

shoes = []
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


def get_shoe_urls():
    url = "https://www.adidas.com/us/nmd-shoes"

    r = requests.get(url, headers=headers)
    html = r.text
    parsed_html = BeautifulSoup(html)
    items = parsed_html.body.find_all('div', attrs={'class': 'image plp-image-bg'})
    for item in items:
        sub_item_url = item.find('a').attrs['href']
        shoes.append(sub_item_url)


def get_size(url):
    r = requests.get(url, headers=headers)
    html = BeautifulSoup(r.text)
    sizes = html.body.find_all('select', attrs={'class': 'size-select'})[0].find_all('option')
    if sizes[0].text.strip(' \t\n\r') == 'Sold out':
        print("%s all sold out" % url)
    else:
        print("%s has below available size: " % url)
        for size in sizes[1:]:
            if size.attrs['data-status'] == 'IN_STOCK':
                print(size.text.strip(' \t\n\r'), end=" ")
        print()


def connect_db():
    try:
        conn = lite.connect("sneakers.db")
        print("Opened database successfully")
        return conn
    except lite.Error as e:
        if conn:
            conn.rollback()
        print("Error %s: " % e.args[0])
        sys.exit(1)


def write_to_database():
    # try:
    con = lite.connect('sneakers.db')
    print("Opened database successfully")


# get_shoe_urls()
#
# for url in shoes:
#     get_size(url)
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def read_sneakers():
    conn = connect_db()
    cursor = conn.cursor()
    conn.row_factory = dict_factory
    cursor.execute("select * from sneakers")
    print(cursor.fetchall())


conn = lite.connect('sneakers.db')
print("Opened database successfully")

cursor = conn.execute("select * from sneakers")

for row in cursor:
    print(row)
