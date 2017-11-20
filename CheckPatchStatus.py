import urllib2
import json

ConvertURL = "https://api.rss2json.com/v1/api.json?rss_url="
RSSFeed = "https://alas.aws.amazon.com/alas.rss"

URL = ConvertURL + RSSFeed

def GetSecurityBulletins():
    response = urllib2.urlopen(URL)
    data = json.loads(response.read())

    print data

    return data['items']


###### Main ###################
def main():
    bulletins = GetSecurityBulletins()

    print bulletins
    return bulletins
