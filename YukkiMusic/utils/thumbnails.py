from config import YOUTUBE_IMG_URL
from youtubesearchpython.future import VideosSearch
import logging
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 10)

print(videosSearch.result())
   
logging.basicConfig(level=logging.INFO)

async def gen_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        logging.error(f"Error generating thumbnail for video ID {videoid}: {e}")
        return YOUTUBE_IMG_URL

async def gen_qthumb(vidid):
    try:
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        logging.error(f"Error generating quick thumbnail for video ID {vidid}: {e}")
        return YOUTUBE_IMG_URL
        
