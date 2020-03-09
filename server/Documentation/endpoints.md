# Client endpoints

## `create_new_account`

Method: `POST`
URL: `localhost:8080/create_new_account/`
Parameters:

| Value    | Type |
|:------- | -------:|
| email | string |
| password | string |
| confirm_password | string |

Body example:

```json
{
	"email": "johndoe@gmail.com",
	"password": "test123",
	"confirm_password": "test123"
}
```

Response example:

```json
{
    "status": 200,
    "msg": "Account created with success !"
}
```

## `is_account_ok`

Method: `POST`
URL: `localhost:8080/is_account_ok/`
Parameters:

| Value    | Type |
|:------- | -------:|
| email | string |
| password | string |

Body example:

```json
{
    "email": "johndoe@gmail.com",
    "password": "test123"
}
```

Response example:

```json
{
    "status": 200,
    "msg": "Account is correct",
    "uuid": "bbaebcd782eb96fe85fcae669762fb"
}
```

## `add_user_area`

Method: `POST`
URL: `localhost:8080/add_user_area/`
Parameters:

| Value    | Type |
|:------- | -------:|
| uuid | string |
| service | string |
| action | string |
| reaction | string |
| action_data | dict |
| reaction_data | dict |

Body example:

* Timer

```json
{
	"uuid": "f5b07829decec02ad9001392da23d4",
	"service": "timer",
	"action": "create_timer",
	"action_data": {
		"time": 60
	},
	"reaction": "send_email",
	"reaction_data": {
		"email": "test@test.com"
	}
}
```

* Weather

```json
{
	"uuid": "8aad97bcec4634ffbac7d78cc769ee",
	"service": "weather",
	"action": "detect_weather",
	"action_data": {
		"city": "Paris"
	},
	"reaction": "send_email",
	"reaction_data": {
		"email": "elliott.heldenbergh@epitech.eu"
	}
}
```

* Youtube

```json
{
	"uuid": "8aad97bcec4634ffbac7d78cc769ee",
	"service": "youtube",
	"action": "detect_new_video",
	"action_data": {
		"channel": "ScienceEtonnante"
	},
	"reaction": "send_email",
	"reaction_data": {
		"email": "elliott.heldenbergh@epitech.eu"
	}
}
```

Response example:

```json
{
    "status": 200,
    "msg": "User services updated !"
}
```

## `get_user_areas`

Method: `GET`
URL: `localhost:8080/get_user_areas/`
Parameters:

| Value    | Type |
|:------- | -------:|
| uuid | string |

Body example:

```json
{
	"uuid": "f5b07829decec02ad9001392da23d4"
}
```

Response example:

```json
{
    "status": 200,
    "msg": "Get user services success !",
    "data": [
        {
            "reaction": "email",
            "service": "timer",
            "action": "create_timer",
            "action_data": {},
            "reaction_data": {}
        }
    ]
}
```

## `delete_user_areas`

Method: `POST`
URL: `localhost:8080/delete_user_areas/`
Parameters:

| Value    | Type |
|:------- | -------:|
| uuid | string |

Body example:

```json
{
	"uuid": "f5b07829decec02ad9001392da23d4"
}
```

Response example:

```json
{
    "status": 200,
    "msg": "User's AREA deleted with success !"
}
```

## `refresh_user_areas`

Method: `POST`
URL: `localhost:8080/refresh_user_areas/`
Parameters:

| Value    | Type |
|:------- | -------:|
| uuid | string |

Body example:

```json
{
	"uuid": "f5b07829decec02ad9001392da23d4"
}
```

Response example:

```json
{
    "status": 200,
    "msg": "User's AREA refreshed with success !"
}
```


## `link_access_token`

Method: `POST`
URL: `localhost:8080/link_access_token/`
Parameters:

| Value    | Type |
|:------- | -------:|
| uuid | string |
| service | string |
| access_token | string |


Body example:

```json
{
	"uuid": "55fccddf5ee0034ff2fda8ebb35813",
	"service": "yammer",
	"access_token": "dbsqd823isdise923ksd"
}
```

Response example:

```json
{
    "status": 200,
    "msg": "Access token linked with success !"
}
```

## `get_user_notifs`

Method: `GET`
URL: `localhost:8080/get_user_notifs/`
Parameters:

| Value    | Type |
|:------- | -------:|
| uuid | string |

Body example:

```json
{
	"uuid": "55fccddf5ee0034ff2fda8ebb35813"
}
```

Response example:

```json
{
    "status": 200,
    "msg":  "Get user notifications success !",
    "data": ["Account created", "Did this...", "Did that..."]
}
```

## Server-side or for development purposes only

## `get_all_accounts`

Method: `GET`
URL: `localhost:8080/get_all_accounts/`
Parameters: No parameters

Response example:

```json
{
    "status": 200,
    "data": [
        {
            "email": "test@test.com",
            "password": "test123"
        }
    ]
}
```

## `reset_indexex`

Method: `POST`
URL: `localhost:8080/reset_indexes/`
Parameters: No parameters

Response example:

```json
{
    "status": 200,
    "msg": "Indexes refreshed with success"
}
```