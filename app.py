import os
import json
import time
import functools
from flask import Flask, request

import lastfm
import lyricswiki

app = Flask(__name__)


def app_api(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        before = time.time()
        try:
            data = fn(*args, **kwargs)
        except:
            result = {'error': 1}
        else:
            result = {'error': 0, 'data': data}
        result['duration'] = time.time() - before
        return json.dumps(result)
    return wrapper


@app.route('/api/lastfm/<user>/recent')
@app_api
def api_recent(user):
    limit = request.args.get('limit', 1)
    return lastfm.get_recent_tracks(user, limit)


@app.route('/api/lyrics/<artist>/<song>')
@app_api
def api_get_lyrics(artist, song):
    return lyricswiki.get_lyrics(artist, song)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
