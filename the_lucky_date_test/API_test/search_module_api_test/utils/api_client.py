import requests
from the_lucky_date_test.API_test.search_module_api_test.config.config_reader import BASE_URL, cookies, \
    cookies_incognito
from the_lucky_date_test.API_test.search_module_api_test.utils.endpoints import GRAPHQL

def like_user(user_id):
    headers = {
        'accept': '*/*',
        'accept-language': 'en,nl-NL;q=0.9,nl;q=0.8,en-US;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=desktop%403.0.252,sentry-public_key=ca47bcda7d02cdd3374dffedb71ab6e5,sentry-trace_id=68b873ec77d140fba410195d231e017a',
        'content-type': 'application/json',
        'origin': 'https://theluckydate.com',
        'priority': 'u=1, i',
        'referer': 'https://theluckydate.com/search',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '68b873ec77d140fba410195d231e017a-9e9804805119da79-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-app-version': '3.0.252',
    }

    json_data = {
        'operationName': 'UserLike',
        'variables': {
            'id': user_id,
        },
        'query': 'mutation UserLike($id: ID!) {\n  likeProfile(idUser: $id) {\n    id\n    interlocutor {\n      id\n      socialConnection: socialConnectionByCurrentUser {\n        id\n        likedByMe\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}',
    }
    return requests.post(BASE_URL + GRAPHQL, cookies=cookies, headers=headers, json=json_data)


def add_to_favorites(user_id):
    headers = {
        'accept': '*/*',
        'accept-language': 'en,nl-NL;q=0.9,nl;q=0.8,en-US;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=desktop%403.0.252,sentry-public_key=ca47bcda7d02cdd3374dffedb71ab6e5,sentry-trace_id=cf447f41f710415896df3f0471510b10',
        'content-type': 'application/json',
        'origin': 'https://theluckydate.com',
        'priority': 'u=1, i',
        'referer': 'https://theluckydate.com/search',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'cf447f41f710415896df3f0471510b10-b9eaf9adb01dbeae-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-app-version': '3.0.252',
        # 'cookie': 'uuid=b65ee479-aa41-4da2-8fd1-f68277061eed; _vwo_uuid_v2=DC03626DD99B2A7D3BAF3659916DB895C|4876b8ff16bed4da3f4d8f49f3f0a315; _gcl_au=1.1.836058042.1743605150; _ga=GA1.1.325209074.1743605150; _fbp=fb.1.1743605149869.82074552244653092; __zlcmid=1QynViJ6X6FXe1O; id_visit=f471ca17-8891-473f-b3f5-3c0a18deeb28; click_time="2025-04-02 20:06:35"; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxZDdmZjZiLTBkYzAtNDQ5YS1iYWJmLTJjYjYwYTQ5ZTA3OCIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzUxNjE3MDQsImlhdCI6MTc0MzYyNTQwNCwibGVnYWN5SWQiOjY1NzQ2OTU3LCJyb2xlIjoibWFya2V0aW5nIiwicm9sZXMiOlsibWFya2V0aW5nIl0sInN1YiI6IjAxSlFWRkVBVllEN0dTREpaNFozSFZDVFRDIiwidmVyIjoiMS4zIn0.ems5sn3LkSAq3W4_R8Uyyrp4TwFfOtbynJfft3dJh80tIVpRv-zbpGBBILcoQ_LIogg-0dgQCIR1qXuss-8arTH9rTciGqfKbxdQZot4dSSUibNOSvAdbjIcZb7zbBzwoxhCm2LNCVuVrBAn9uE7YPzgp0-ooN2J66yy1_4Uxs0-qVv3zADuGp6y1g1rMu5G73psN1sFpwdzVoJvZFjuVDWer1477SX5qubwf3bpUrlAgRO9xJaZ91CyPzlMRzxGQKs9SXV5b9MZ7YDWXTv5vFt0LU8nfKe9y_kW_t1S05iCTdvgWC6yLNskfgEnB8yTtgCq3uteIOjtbfaG7raaFmr2OVPahyuX_IN12nV7oN2ypZTbiU2YMPNByGLk4S16vqAxM0Pz1__wMUxW-jrdrdLzN6zdvpDWnv4tmlnGqjIPeYSfAsruv-YeLWS7wFOJfKalKGfp287rhbPQ9KMv7Dt8HTL6cErNkP1KaVLleT1vPiOmVoTEDWVd7wUYOmJzSst5Z3hVbPVppmlc_OFRH50aBbID4Suq--M3LtQbK1jpOMvkPLnFJB-PWXlv2oZtREhPeBawjn130cMjfLAcZ3Sq-l9k0ExQLoThrOaecozShbFQN9_0oNQ1RqXS0bEB57AOSKlwx6nhbsB17ZMTxoLV68qriz1FG84XMqMRFOU; cc_cookie=%7B%22required%22%3A1%2C%22marketing%22%3A1%7D; _csrf=KVM6_0hoGA1iw4JswD5Yg_DDmyu-h9Q_; _ga_GHGWEFY67R=GS1.1.1743693860.8.1.1743694947.60.0.0',
    }
    json_data = {
        'operationName': 'UserFavorite',
        'variables': {
            'id': user_id,
        },
        'query': 'mutation UserFavorite($id: ID!) {\n  favoriteProfile(idUser: $id) {\n    id\n    interlocutor {\n      ...UserBasic\n      avatar {\n        id\n        url: xxl\n        __typename\n      }\n      socialConnection: socialConnectionByCurrentUser {\n        id\n        favoritedByMe\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserBasic on User {\n  id\n  name\n  isOnline\n  profile {\n    id\n    city {\n      id\n      name\n      __typename\n    }\n    country {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  __typename\n}',
    }
    return requests.post(BASE_URL + GRAPHQL, cookies=cookies, headers=headers, json=json_data)


def search_users(criteria=None,limit=None):
    headers = {
        'accept': '*/*',
        'accept-language': 'en,nl-NL;q=0.9,nl;q=0.8,en-US;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=desktop%403.0.252,sentry-public_key=ca47bcda7d02cdd3374dffedb71ab6e5,sentry-trace_id=cfe46a95c3aa411a96f7e10be90c9ee3',
        'content-type': 'application/json',
        'origin': 'https://theluckydate.com',
        'priority': 'u=1, i',
        'referer': 'https://theluckydate.com/search',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'cfe46a95c3aa411a96f7e10be90c9ee3-b8ae38f39cd7998f-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-app-version': '3.0.252',
        # 'cookie': 'uuid=b65ee479-aa41-4da2-8fd1-f68277061eed; _vwo_uuid_v2=DC03626DD99B2A7D3BAF3659916DB895C|4876b8ff16bed4da3f4d8f49f3f0a315; _gcl_au=1.1.836058042.1743605150; _ga=GA1.1.325209074.1743605150; _fbp=fb.1.1743605149869.82074552244653092; __zlcmid=1QynViJ6X6FXe1O; id_visit=f471ca17-8891-473f-b3f5-3c0a18deeb28; click_time="2025-04-02 20:06:35"; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxZDdmZjZiLTBkYzAtNDQ5YS1iYWJmLTJjYjYwYTQ5ZTA3OCIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzUxNjE3MDQsImlhdCI6MTc0MzYyNTQwNCwibGVnYWN5SWQiOjY1NzQ2OTU3LCJyb2xlIjoibWFya2V0aW5nIiwicm9sZXMiOlsibWFya2V0aW5nIl0sInN1YiI6IjAxSlFWRkVBVllEN0dTREpaNFozSFZDVFRDIiwidmVyIjoiMS4zIn0.ems5sn3LkSAq3W4_R8Uyyrp4TwFfOtbynJfft3dJh80tIVpRv-zbpGBBILcoQ_LIogg-0dgQCIR1qXuss-8arTH9rTciGqfKbxdQZot4dSSUibNOSvAdbjIcZb7zbBzwoxhCm2LNCVuVrBAn9uE7YPzgp0-ooN2J66yy1_4Uxs0-qVv3zADuGp6y1g1rMu5G73psN1sFpwdzVoJvZFjuVDWer1477SX5qubwf3bpUrlAgRO9xJaZ91CyPzlMRzxGQKs9SXV5b9MZ7YDWXTv5vFt0LU8nfKe9y_kW_t1S05iCTdvgWC6yLNskfgEnB8yTtgCq3uteIOjtbfaG7raaFmr2OVPahyuX_IN12nV7oN2ypZTbiU2YMPNByGLk4S16vqAxM0Pz1__wMUxW-jrdrdLzN6zdvpDWnv4tmlnGqjIPeYSfAsruv-YeLWS7wFOJfKalKGfp287rhbPQ9KMv7Dt8HTL6cErNkP1KaVLleT1vPiOmVoTEDWVd7wUYOmJzSst5Z3hVbPVppmlc_OFRH50aBbID4Suq--M3LtQbK1jpOMvkPLnFJB-PWXlv2oZtREhPeBawjn130cMjfLAcZ3Sq-l9k0ExQLoThrOaecozShbFQN9_0oNQ1RqXS0bEB57AOSKlwx6nhbsB17ZMTxoLV68qriz1FG84XMqMRFOU; cc_cookie=%7B%22required%22%3A1%2C%22marketing%22%3A1%7D; _csrf=KVM6_0hoGA1iw4JswD5Yg_DDmyu-h9Q_; _ga_GHGWEFY67R=GS1.1.1743693860.8.1.1743695160.51.0.0',
    }

    if criteria and limit is None:
        criteria = {
            'ageFrom': 0,
            'ageTo': 100,
            'country': '',
            'onlyOnline': False
        }
        limit = 10
    json_data = {
        'operationName': 'SearchUsers',
        'variables': {
            'criteria': criteria,
            'limit': limit,
            'cursor': '',
        },
        'query': 'query SearchUsers($criteria: SearchCriteriaInput, $cursor: String, $limit: Int) {\n  currentUser {\n    id\n    searchUsers(criteria: $criteria, cursor: $cursor, limit: $limit) {\n      users {\n        ...UserBasic\n        avatar {\n          id\n          url: xxl\n          __typename\n        }\n        profile {\n          id\n          dateBirth\n          __typename\n        }\n        publicPhotos {\n          id\n          url: standard\n          __typename\n        }\n        privatePhotos {\n          id\n          url: standard\n          __typename\n        }\n        __typename\n      }\n      cursor\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserBasic on User {\n  id\n  name\n  isOnline\n  profile {\n    id\n    city {\n      id\n      name\n      __typename\n    }\n    country {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  __typename\n}',
    }
    return requests.post(BASE_URL + GRAPHQL, cookies=cookies_incognito, headers=headers, json=json_data)


def next_user_card(user_id):
    headers = {
        'accept': '*/*',
        'accept-language': 'en',
        'baggage': 'sentry-environment=production,sentry-release=desktop%403.0.252,sentry-public_key=ca47bcda7d02cdd3374dffedb71ab6e5,sentry-trace_id=9658d6fb4919476cb077de83a26bf07d',
        'content-type': 'application/json',
        'origin': 'https://theluckydate.com',
        'priority': 'u=1, i',
        'referer': 'https://theluckydate.com/search',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '9658d6fb4919476cb077de83a26bf07d-a44a6a2d583231b3-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-app-version': '3.0.252',
        # 'cookie': 'uuid=bde63887-d664-4c8b-bfb1-17245e1d8748; id_visit=7f83aa3b-a6b1-427b-968c-f625cc814ce8; _vwo_uuid_v2=D9715AE2B8A23CF502C33965492069F5A|39bda9603f8732b8a79ae1b8527acd90; click_time="2025-04-03 16:25:39"; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxZDdmZjZiLTBkYzAtNDQ5YS1iYWJmLTJjYjYwYTQ5ZTA3OCIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzUyMzM1NTMsImlhdCI6MTc0MzY5NzI1MywibGVnYWN5SWQiOjY1NzQ2OTU3LCJyb2xlIjoibWFya2V0aW5nIiwicm9sZXMiOlsibWFya2V0aW5nIl0sInN1YiI6IjAxSlFWRkVBVllEN0dTREpaNFozSFZDVFRDIiwidmVyIjoiMS4zIn0.brFDX2rA6Z-BV02cMyzNT_Zs4EhYK5tldy3Aeh6foePL3DkzqnfjeR0YItV7qtPllV4SDISAuMgH7OTSHUMDGhydOjW875R42eHrlnMRMQe9XhT-S5OUX0QnaFep-IA8f2sfnYlc8ICxLUASESMitNeM3ye3O9hefyu-nwqP4mYfa4D4m6CSXUEkRjUbHPkMZhDQvJUpf3dLj4h1DmWwGsyCYTeGo73vyy_sXcLhnzF61hzMmZid6ESjclEDJTqrDTmFURJmniiJjrLxYSB_9CHxUel0h8CDErTOy8biBkifJ1YL27tqG34pRs8ZMpI6poTj_xEBzPZ66upE7B4LIN98cDqmyUAmE4EZ9Jyd_oVYYVDhUjVVgeX9istg51kyO19KurSTcJOKTE7aB-oqaC0WY7hT2ztnrpKByk-ecv7W5iOV8C7uwpRHt7DIAfMBRMf1V4vcN6hAZtqkLjPEycnBAPexf0gDV4729celUyZOCT_JBP1k5ODU1geLDerBwlWjdY8xAORuZuygk0fBFy9u0OkQ3gkACZlGW_lN7fz0Q975qmU1vM-frvY58iipTgRMOPm4mb1SzefIQxVqJekKDplqXzVhS2Uq8DqXtCC9izaj0MqvVMH8lwaCr9fkD07cYOXcA5kfYZbWasUAfb7fksiJknyoVwihbksKFrQ; cc_cookie=%7B%22required%22%3A1%2C%22marketing%22%3A1%7D; _gcl_au=1.1.1393758890.1743697554; _ga=GA1.1.527533335.1743697555; _fbp=fb.1.1743697555214.480732796113381368; _csrf=RRGPwsYfsTETTz6et-ixa8jcF4QD9U0K; __zlcmid=1QynViJ6X6FXe1O; _ga_GHGWEFY67R=GS1.1.1743697554.1.1.1743697936.60.0.0',
    }
    json_data = {
        'operationName': 'UserConnectionWith',
        'variables': {
            'id': user_id,
        },
        'query': 'query UserConnectionWith($id: ID!) {\n  user(id: $id) {\n    id\n    socialConnection: socialConnectionByCurrentUser {\n      id\n      likedByMe\n      blockedByMe\n      blockedByInterlocutor\n      favoritedByMe\n      __typename\n    }\n    __typename\n  }\n}',
    }

    return requests.post('https://theluckydate.com/graphql', cookies=cookies, headers=headers, json=json_data)


def profile_btn_card(user_id):
    headers = {
        'accept': '*/*',
        'accept-language': 'en,nl-NL;q=0.9,nl;q=0.8,en-US;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=desktop%403.0.252,sentry-public_key=ca47bcda7d02cdd3374dffedb71ab6e5,sentry-trace_id=4e83ea874fe24e9a90cd942e6ef26f6a,sentry-sample_rate=0,sentry-transaction=profile,sentry-sampled=false',
        'content-type': 'application/json',
        'origin': 'https://theluckydate.com',
        'priority': 'u=1, i',
        'referer': 'https://theluckydate.com/user/0001ET4F58GEEYH3KE52CFTXMC',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '4e83ea874fe24e9a90cd942e6ef26f6a-912144c87d35a2bc-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-app-version': '3.0.252',
        # 'cookie': 'uuid=b65ee479-aa41-4da2-8fd1-f68277061eed; _vwo_uuid_v2=DC03626DD99B2A7D3BAF3659916DB895C|4876b8ff16bed4da3f4d8f49f3f0a315; _gcl_au=1.1.836058042.1743605150; _ga=GA1.1.325209074.1743605150; _fbp=fb.1.1743605149869.82074552244653092; __zlcmid=1QynViJ6X6FXe1O; id_visit=f471ca17-8891-473f-b3f5-3c0a18deeb28; cc_cookie=%7B%22required%22%3A1%2C%22marketing%22%3A1%7D; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxZDdmZjZiLTBkYzAtNDQ5YS1iYWJmLTJjYjYwYTQ5ZTA3OCIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzUzMDcyNDAsImlhdCI6MTc0Mzc3MDk0MCwibGVnYWN5SWQiOjY1NzQ2OTU3LCJyb2xlIjoibWFya2V0aW5nIiwicm9sZXMiOlsibWFya2V0aW5nIl0sInN1YiI6IjAxSlFWRkVBVllEN0dTREpaNFozSFZDVFRDIiwidmVyIjoiMS4zIn0.CJFbscnycqnoMDBYtul9otfNya5mvbZ8MuSXMO3a_fhvhnGGNcAwQfSj-HwCnnljjDz49C4PXAUfc5sqPhOdmjNT-tWdTGno3bWJcUJ-DftFHc-VQVLccaD1IedppE3K8VkAXaLjNdr_OEPeR8jeyPEtlKJOQVwPKrd2suyKTRdsEEzLvF3WyUxUXJOq0CpwFLiG_hscd_pogIpXhicb4z12PF6vAhbuFik5GcjUxZR6tnOM8vXt6nagL8wtxEVL-g7ILLvtacF7GeMV92LbBtpDqU3Yrsx2-WwHRGjGZzaL2V9qch4e8ykbSxn1JnhfhAlQDXpoqL6T5febr_cePAl6yhbkAqVbctVIt8_5-xSuHgN8_5RYEhG4sZ-rbxZzutT4BcLwO1rI0cekdtePYCLJLII3NbIQO8ekc-qRu4PkVVT2lc0B36vLtLfq71Yl_aNTGGnkm0FZrTWDvncG0A26DsvqHFO7CDfOTeDsYYIZhXAWe9uxQmm7V3qCzBE99bx52bYn9GWNFRv7HqdFJnBG5xg0k49dtoQVPaQ0Av25drJMu3L8tNQT47jrLwNiovTON9jkWRb2q8NoXHVfGAeSl0Ko-G2LwxjcD6o-kWP_vZiyCYbMSUivZZu1AORfeMWDUGx-i4DCyASHsnaXahkvA0KUh-o6CISzRNp_PME; _csrf=9Nqr31T21F13tvApvPo2zOyBvkDpZ8gT; _ga_GHGWEFY67R=GS1.1.1743771239.10.1.1743771544.56.0.0',
    }
    json_data = {
        'operationName': 'User',
        'variables': {
            'id': user_id,
        },
        'query': 'query User($id: ID!) {\n  user(id: $id) {\n    id\n    name\n    legacyId\n    isBlocked\n    isOnline\n    avatar {\n      id\n      url: xxl\n      __typename\n    }\n    profile {\n      id\n      canReceiveGift\n      city {\n        id\n        name\n        __typename\n      }\n      country {\n        id\n        name\n        __typename\n      }\n      countChildren\n      dateBirth\n      description\n      drinking\n      education\n      height\n      isVerified\n      occupation\n      smoking\n      weight\n      interests\n      __typename\n    }\n    avatar {\n      ...ProfilePhoto\n      standard\n      __typename\n    }\n    publicPhotos {\n      ...ProfilePhoto\n      standard\n      __typename\n    }\n    privatePhotos {\n      ...ProfilePhoto\n      blurredThumbnail\n      __typename\n    }\n    videoAvatar {\n      ...ProfileVideo\n      __typename\n    }\n    publicVideos {\n      ...ProfileVideo\n      __typename\n    }\n    videos: paidIntroVideos {\n      ...ProfilePaidVideo\n      __typename\n    }\n    socialConnection: socialConnectionByCurrentUser {\n      id\n      likedByMe\n      blockedByMe\n      blockedByInterlocutor\n      favoritedByMe\n      hasDialog\n      __typename\n    }\n    story {\n      id\n      timeLeft\n      isViewedByCurrentUser\n      __typename\n    }\n    virtualGiftsFromCurrentUser {\n      id\n      url\n      __typename\n    }\n    virtualGiftCategories {\n      id\n      gifts {\n        id\n        url\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ProfilePhoto on Photo {\n  id\n  type\n  url: xxl\n  original(watermark: {key: "shpzkl5ie2t30it1q", position: BOTTOM_RIGHT})\n  __typename\n}\n\nfragment ProfileVideo on Video {\n  id\n  mp4Sd\n  mp4Hd\n  thumbnail\n  __typename\n}\n\nfragment ProfilePaidVideo on PaidVideo {\n  id\n  thumbnail\n  isPurchasedByCurrentUser\n  video {\n    id\n    mp4Hd\n    mp4Sd\n    __typename\n  }\n  __typename\n}',
    }


    return requests.post('https://theluckydate.com/graphql', cookies=cookies, headers=headers, json=json_data)


def user_connection_with(user_id): # note выбор маленькой карточки с фото юзера
    headers = {
        'accept': '*/*',
        'accept-language': 'en,nl-NL;q=0.9,nl;q=0.8,en-US;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=desktop%403.0.252,sentry-public_key=ca47bcda7d02cdd3374dffedb71ab6e5,sentry-trace_id=ae5d5e5133204948aa3f0b68cd7249a7',
        'content-type': 'application/json',
        'origin': 'https://theluckydate.com',
        'priority': 'u=1, i',
        'referer': 'https://theluckydate.com/search',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'ae5d5e5133204948aa3f0b68cd7249a7-9201c600387966a3-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'x-app-version': '3.0.252',
        # 'cookie': 'uuid=b65ee479-aa41-4da2-8fd1-f68277061eed; _vwo_uuid_v2=DC03626DD99B2A7D3BAF3659916DB895C|4876b8ff16bed4da3f4d8f49f3f0a315; _gcl_au=1.1.836058042.1743605150; _ga=GA1.1.325209074.1743605150; _fbp=fb.1.1743605149869.82074552244653092; __zlcmid=1QynViJ6X6FXe1O; id_visit=f471ca17-8891-473f-b3f5-3c0a18deeb28; cc_cookie=%7B%22required%22%3A1%2C%22marketing%22%3A1%7D; token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImMxZDdmZjZiLTBkYzAtNDQ5YS1iYWJmLTJjYjYwYTQ5ZTA3OCIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NzUzMDcyNDAsImlhdCI6MTc0Mzc3MDk0MCwibGVnYWN5SWQiOjY1NzQ2OTU3LCJyb2xlIjoibWFya2V0aW5nIiwicm9sZXMiOlsibWFya2V0aW5nIl0sInN1YiI6IjAxSlFWRkVBVllEN0dTREpaNFozSFZDVFRDIiwidmVyIjoiMS4zIn0.CJFbscnycqnoMDBYtul9otfNya5mvbZ8MuSXMO3a_fhvhnGGNcAwQfSj-HwCnnljjDz49C4PXAUfc5sqPhOdmjNT-tWdTGno3bWJcUJ-DftFHc-VQVLccaD1IedppE3K8VkAXaLjNdr_OEPeR8jeyPEtlKJOQVwPKrd2suyKTRdsEEzLvF3WyUxUXJOq0CpwFLiG_hscd_pogIpXhicb4z12PF6vAhbuFik5GcjUxZR6tnOM8vXt6nagL8wtxEVL-g7ILLvtacF7GeMV92LbBtpDqU3Yrsx2-WwHRGjGZzaL2V9qch4e8ykbSxn1JnhfhAlQDXpoqL6T5febr_cePAl6yhbkAqVbctVIt8_5-xSuHgN8_5RYEhG4sZ-rbxZzutT4BcLwO1rI0cekdtePYCLJLII3NbIQO8ekc-qRu4PkVVT2lc0B36vLtLfq71Yl_aNTGGnkm0FZrTWDvncG0A26DsvqHFO7CDfOTeDsYYIZhXAWe9uxQmm7V3qCzBE99bx52bYn9GWNFRv7HqdFJnBG5xg0k49dtoQVPaQ0Av25drJMu3L8tNQT47jrLwNiovTON9jkWRb2q8NoXHVfGAeSl0Ko-G2LwxjcD6o-kWP_vZiyCYbMSUivZZu1AORfeMWDUGx-i4DCyASHsnaXahkvA0KUh-o6CISzRNp_PME; _csrf=9Nqr31T21F13tvApvPo2zOyBvkDpZ8gT; _ga_GHGWEFY67R=GS1.1.1743771239.10.1.1743772743.25.0.0',
    }

    json_data = {
        'operationName': 'UserConnectionWith',
        'variables': {
            'id': user_id,
        },
        'query': 'query UserConnectionWith($id: ID!) {\n  user(id: $id) {\n    id\n    socialConnection: socialConnectionByCurrentUser {\n      id\n      likedByMe\n      blockedByMe\n      blockedByInterlocutor\n      favoritedByMe\n      __typename\n    }\n    __typename\n  }\n}',
    }

    return requests.post('https://theluckydate.com/graphql', cookies=cookies, headers=headers, json=json_data)
