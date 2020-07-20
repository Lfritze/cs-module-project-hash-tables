# BUild a client that will cache a URL

# 1st request go out to internet
# 2nd request: return from the cache

# How to implement our cache using a hash table aka a dict
# What are our keys,   the URL !!
# and what are our values?
import urllib.request
import datetime

cache = {}
url="https://www.google.com"

class CacheEntry:
  def __init__(self, data):
    self.data = data
    self.time_fetched = datetime.datetime.now().timestamp()

### given a url, check if its in the cache
def fetch_web_page(url):
  stale_data = True
  if url in cache:
    time_now = datetime.datetime.now().timestamp()
    print("getting from cache")
    cache_entry = cache[url]
    if time_now - cache_entry.time_fetched < 10:
      page = cache_entry.data
      stale_data = False

  elif stale_data:
    print("getting from internet")
## otherwise, send out a request to get the web page 
    response = urllib.request.urlopen(url)
    data = response.read()
    response.close()

### and put result in our cache
    cache_entry = CacheEntry(data)
    cache[url] = data
    page = cache[url].data
  return page

page = fetch_web_page(url)
print(page)

also_page = fetch_web_page(url)

# One issue is memory, lots of urls will fill memory
## if the page isnt requested in a while, delete
# LRU cache
# Use time to delete really old data



# What if the page changes? 
# Store time, and if data is stale, re-fetch





