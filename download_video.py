import urllib.request
import re

url = "https://www.pexels.com/search/videos/wearing%20baseball%20cap/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    links = re.findall(r'https://player\.vimeo\.com/external/[^"\'\s]+\.mp4[^"\'\s]*', html)
    if not links:
        links = re.findall(r'https://images\.pexels\.com/video-files/[^"\'\s]+\.mp4', html)
    
    if links:
        video_url = links[0]
        print("Found video URL:", video_url)
        urllib.request.urlretrieve(video_url, "DB Sneakers/assets/video/hat-tryon.mp4")
        print("Video downloaded successfully!")
    else:
        print("No mp4 links found on page.")
except Exception as e:
    print("Error:", e)
