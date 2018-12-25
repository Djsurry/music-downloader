# music-downloader
Downloads music to be added to spotify


## Setup
1. Dependacies
    - `youtube_dl`, `pip3 install youtube_dl`
    - `BeautifulSoup`, `pip3 install beautifulsoup4`
2. Environment Variables
    - You have to export the envirnment variable `MUSIC`. This is the directory where the songs will be downloaded
    - `export MUSIC=/Users/david/Music/import-to-spotify`
3. Spotify
    - On desktop, go to `Settings -> Local Files -> Add source`. Select the file you exported in the environment varible earlier

## Usage
Simply run the file with `python3 download.py`. It will then prompt you for input. The choices are as follows
1. URL
    - this url must be in the format `https://youtube.com/watch?v=SOMEVIDEO`
    - Will download directly from this video
2. Search Query
    - You can also enter a search, such as `forever drake`. This will take the top result
    - Anything that doesnt match the url format will be treated as a search query
The file will be downloaded and moved the the directory specified in the `MUSIC` env variable. Then it will show up in spotify to be added to playlists

## Troubleshootting
1. Make sure url is legitamate. Use a web browser to check
2. Make sure your env varible is exported correctly, try `echo $MUSIC` and make sure its what you want
3. Refresh spotify local files by disabling your folder and re enabling it in `Settings -> Local Files`



