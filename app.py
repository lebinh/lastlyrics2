import os
import time
import functools
from flask import Flask, request, jsonify

import lastfm
import lyricswiki

app = Flask(__name__)


def app_api(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        before = time.time()
        data = fn(*args, **kwargs)
        duration = time.time() - before
        resp = jsonify(data=data)
        resp.headers['Duration'] = duration
        return resp
    return wrapper


@app.route('/api/recenttracks/<user>')
@app_api
def get_recent_tracks(user):
    limit = request.args.get('limit', 1)
    return lastfm.get_recent_tracks(user, limit)


@app.route('/api/lyrics/<artist>/<song>')
@app_api
def get_lyrics(artist, song):
    return dict(lyrics=lyricswiki.get_lyrics(artist, song))


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
