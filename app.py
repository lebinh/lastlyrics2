import os
import json
import time
import functools
from flask import Flask, request

import lastfm

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
        duration = time.time() - before
        result['duration'] = duration
        return json.dumps(result)
    return wrapper


@app.route('/api/<user>/recent')
@app_api
def api_recent(user):
    limit = request.args.get('limit', 1)
    return lastfm.get_recent_tracks(user, limit)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
