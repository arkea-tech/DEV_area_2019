about = {
    "client": {
        "host": ""
    },
    "server": {
        "current_time": "",
        "services": [{
            "name": "timer",
            "actions": [{
                "name": "create_timer",
                "description": "The user define a timer of N secondes"
            }, {
                "name": "restart_timers",
                "description": "The user restarts all his timers"
            }],
            "reactions": [{
                "name": "send_email",
                "description": "The user is notified by email that his timer has ended"
            }]
        }, {
            "name": "weather",
            "actions": [{
                "name": "detect_weather",
                "description": "Detects if the weather is changing in a specified city"
            }, {
                "name": "detect_temperature",
                "description": "Detects if the temperature is changing"
            }, {
                "name": "detect_wind_speed",
                "description": "Detects if the wind speed is changing"
            }, {
                "name": "detect_wind_direction",
                "description": "Detects if the wind direction is changing"
            }, {
                "name": "detect_humidity",
                "description": "Detects if the humidity level is changing"
            }],
            "reactions": [{
                "name": "send_email",
                "description": "The user is notified by email that some weather changes are occuring"
            }]
        }, {
            "name": "github",
            "actions": [{
                "name": "detect_new_repository",
                "description": "Detect if a new event has been created"
            }, {
                "name": "detect_new_follower",
                "description": "Detect if an event is planned today"
            }, {
                "name": "detect_new_following",
                "description": "Detect if an event is planned today"
            }],
            "reactions": [{
                "name": "send_email",
                "description": "The user is notified by email that an event has been created"
            }]
        }, {
            "name": "mail",
            "actions": [{}],
            "reactions": [{
                "name": "send_email",
                "description": "The user receives a custom email depending on action choosen"
            }]
        }, {
            "name": "youtube",
            "actions": [{
                "name": "detect_new_video",
                "description": "Detect if a new video has been uploaded"
            }, {
                "name": "detect_new_comment",
                "description": "Detect if a new comment has been posted on a video"
            }, {
                "name": "detect_new_like",
                "description": "Detect if a new like has been posted on a video"
            }, {
                "name": "detect_new_dislike",
                "description": "Detect if a new dislike has appeared on a video"
            }, {
                "name": "detect_new_view",
                "description": "Detect if a new view has appeared on a video"
            }, {
                "name": "detect_new_subscriber",
                "description": "Detect if a channel have new subscribers"
            }],
            "reactions": [{
                "name": "send_email",
                "description": "The user is notified by email that a new video has been uploaded"
            }]
        }, {
            "name": "reddit",
            "actions": [{
                "name": "detect_new_subreddit_post",
                "description": "Detect if a new post has appeared in a subreddit"
            }, {
                "name": "detect_new_subreddit_comment",
                "description": "Detect if a new post has appeared in a subreddit"
            }, {
                "name": "detect_new_user_post",
                "description": "Detect if a new post has appeared in a subreddit"
            }, {
                "name": "detect_new_user_comment",
                "description": "Detect if a new post has appeared in a subreddit"
            }],
            "reactions": [{
                "name": "send_email",
                "description": "The user is notified by email that his timer has ended"
            }]
        }, {
            "name": "deezer",
            "actions": [{
                "name": "detect_new_album",
                "description": "Detect if an artist has released a new album"
            }, {
                "name": "detect_new_artist_fans",
                "description": "Detect if an artist got new fans"
            }, {
                "name": "detect_new_playlist_fans",
                "description": "If new fans has subsribers to a playlist"
            }, {
                "name": "detect_new_playlist_track",
                "description": "Detect if a new track has appeared in a playlist"
            }],
            "reactions": [{
                "name": "send_email",
                "description": "The user is notified by email that his timer has ended"
            }]
        }]
    }
}
