import urllib.request
import re

url = "https://mixkit.co/free-stock-video/hat/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    links = re.findall(r'https://assets\.mixkit\.co/videos/preview/[^"\'\s]+\.mp4', html)
    if links:
        print("Found:", links[0])
        urllib.request.urlretrieve(links[0], "DB Sneakers/assets/video/hat-tryon.mp4")
    else:
        print("No mixkit links found")
except Exception as e:
    print("Error:", e)
