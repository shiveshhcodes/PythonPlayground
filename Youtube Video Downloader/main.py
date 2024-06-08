import ssl
import certifi

ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# Your existing code
from pytube import YouTube

YouTube_1 = YouTube("https://www.youtube.com/watch?v=giYejigUM9A")
print("The Title of Video is " , YouTube_1.title)
print(YouTube_1.thumbnail_url)
# print(YouTube_1.views)
# print(YouTube_1.author)
