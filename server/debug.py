
import json

from Components.youtube_service import Youtube

y = Youtube()

last = y.search_video_by_name("Science etonnante est-il nefaste ?")
# print(json.dumps(last, indent=4))
video_id = last['id']['videoId']
video_info = y.get_video_info_by_id(video_id)
print(json.dumps(video_info, indent=4))

# channel = y.search_channel_by_name("Science Etonnante")
# print(json.dumps(channel, indent=4))
# stats = y.get_channel_stats(channel['id']['channelId'])
# print(json.dumps(stats, indent=4))
