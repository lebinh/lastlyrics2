import requests
from pyquery import PyQuery as pq


API_ROOT = 'http://ws.audioscrobbler.com/2.0/'
API_KEY = '4b07bbcee2b8fc6f56a338ad24cbdedf'


def last_query(method=None, **kwargs):
    params = dict(**kwargs)
    params['method'] = method
    params['api_key'] = API_KEY
    return requests.get(API_ROOT, params=params)


def parse_track(element):
    track = pq(element)
    return {
        'name': track('name').text(),
        'artist': track('artist').text(),
        'time': track('date').attr['uts']
    }


def get_recent_tracks(user, limit=1):
    """ Get recently scrobbed tracks by given user """
    resp = last_query('user.getrecenttracks', user=user, limit=limit)
    if resp.status_code == 200:
        doc = pq(resp.content)
        return [parse_track(ele) for ele in doc('track')]
    return None
