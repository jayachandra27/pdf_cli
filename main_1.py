import requests
from bs4 import BeautifulSoup
import re
import sys
import click

@click.command()
@click.option('--book_name',help="file name that you want to download")
def download(book_name):
    book = requests.get('https://www.pdfdrive.com/search?q={}&pagecount=&pubyear=&searchin=&em='.format(book_name))
    if book.status_code == 200:
        print("search successful- fecthing your pdf content\n")
        soup = BeautifulSoup(book.text, "lxml")
        file_id = soup.find_all("div",class_="file-left")
        file_info = file_id[0].find("a")["href"]
        print("Hitting the database to get the pdf content\n")
        download_link = requests.get('https://www.pdfdrive.com{}'.format(file_info))
        session_soup = BeautifulSoup(download_link.text, "lxml")
        session_info = session_soup.find_all('div',class_='ebook-buttons')
        x = session_info[0].find('button')['data-preview'].split("=")[1].split("&")[0]
        y = session_info[0].find('button')['data-preview'].rsplit("session=")[1]
        file_name = re.split('-([a-z]\d)',file_info)[0].split('/')[1] + ".pdf"
        print("getting and parsing session_info\n")
        pdf = requests.get('https://pdfdrive.com/download.pdf?id={}&h={}&u=cache&amp;ext=pdf'.format(x, y))
        total_length = pdf.headers.get('content-length')
        with open(file_name,'wb') as p:
            print("downloading pdf of your choice: {}".format(file_name))
            p.write(pdf.content)
            dl = 0
            total_length = int(total_length)
            for data in pdf.iter_content(chunk_size=4096):
                dl += len(data)
                p.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
            print("\n YAY.. Download Successful......")
    else:
        print("PDF missing or does not exist in the database, search with a better keyword")



if __name__ == '__main__':
    download()
