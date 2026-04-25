import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.youtube.com/results?search_query=fitted+hat+streetwear+fashion+b-roll"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    ids = re.findall(r'"videoId":"([^"]{11})"', html)
    if ids:
        # Get first real video ID (often first few are real)
        print("Found YouTube ID:", ids[0])
    else:
        print("No IDs found")
except Exception as e:
    print("Error:", e)
