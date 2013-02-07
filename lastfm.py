import requests


API_ROOT = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = '4b07bbcee2b8fc6f56a338ad24cbdedf'


def last_query(method=None, **kwargs):
    params = dict(**kwargs)
    params['method'] = method
    params['api_key'] = API_KEY
    params['format'] = 'json'
    return requests.get(API_ROOT, params=params)


def extract_data(track):
    return {
        'song': track['name'],
        'artist': track['artist']['#text'],
        'time': track['date']['uts']
    }


def get_recent_tracks(user, limit=1):
    """ Get recently scrobbed tracks by given user """
    resp = last_query('user.getrecenttracks', user=user, limit=limit)
    if resp.status_code == 200:
        recent = resp.json().get('recenttracks')
        if recent:
            tracks = recent['track']
            if isinstance(tracks, list):
                return [extract_data(track) for track in tracks]
            else:
                return [extract_data(tracks)]
    return []
