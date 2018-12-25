from bs4 import BeautifulSoup
import os, youtube_dl, requests

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]

}

def get_top(search):
    # construct search url. The weird split/join thing replaces spaces and linebreaks with '+'
    url = f"https://youtube.com/results?search_query={'+'.join(search.split())}"
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, 'lxml')
    links = []
    for link in soup.find_all('a'):
        if "watch" in link.get('href'):
            links.append(link.get('href'))
    result = f"https://youtube.com{links[0]}" if len(links) != 0 else None
    return result

def download(url):
    print(f"URL: {url}")
    old_dir = os.listdir()
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    

    filename = [n for n in os.listdir() if n not in old_dir][0]
    
    # escaping spaces
    escaped_filename = "\\ ".join(filename.split(' '))
    # escaping ()
    escaped_filename = "\\(".join(escaped_filename.split('('))
    escaped_filename = "\\)".join(escaped_filename.split(')'))
    # gets index of last '-'
    index = list(reversed(escaped_filename)).index('-')
    # take everything before that index as youtube_dl adds on random characters at the end
    new = escaped_filename[:len(escaped_filename)-index-1] + '.mp3'
    # renames file
    os.system("mv {old} {new}".format(old=escaped_filename, new=new))
    return new

def main():
    if not os.getenv("MUSIC"):
        print("Please export the envirnment varible music. Exiting...")
        exit()
    if "downloaded-music" in os.listdir():
        print("Please move or rename the file downloaded-music from the CWD. Exiting...")
        exit()

    query = input("Search video or direct youtube link: ")
    if "https://" in query and 'youtube' in query and 'watch' in query:
        good = False
        try:
            r = requests.get(query)
            good = True
        except:
            pass
        if good and r.status_code == 200:
            file = download(query)
    else:
        url = get_top(query)
        if url:
            print("HERE")
            file = download(url)
        else:
            print("Invalid search term. Exiting...")
            quit()
    print("Got file, {}".format(file))
    print("moving file to {}".format(os.getenv("MUSIC")))
    os.system("mv {filename} {dir}".format(filename=file, dir=os.getenv("MUSIC")))
main()