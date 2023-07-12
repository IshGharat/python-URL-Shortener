import pyshorteners

url=input("\nEnter the URL: ")

def shorten_URL(URL):
    s = pyshorteners.Shortener()
    print("\nShortened URL: ",s.tinyurl.short(URL))

shorten_URL(url)