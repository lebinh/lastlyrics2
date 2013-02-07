import lxml
import requests
from pyquery import PyQuery as pq


BASE_LYRICS_URL = 'http://lyrics.wikia.com/'
API_ROOT = 'http://lyrics.wikia.com/api.php'


def to_title_case(name):
    """ Convert name to Title_Case_Name """
    return '_'.join([word.capitalize() for word in name.split()])


def get_lyrics_page_url(artist, song):
    """ Return Wikia Lyrics's url for given song """
    page = artist.capitalize() + ':' + to_title_case(song)
    return BASE_LYRICS_URL + page


def get_lyrics_content(e):
    """ Return content if given element is an element with lyrics """
    if isinstance(e, lxml.html.HtmlElement):
        if e.tag == 'br':
            return u'\n'
        return None
    if isinstance(e, lxml.etree._ElementStringResult):
        return unicode(e)
    if isinstance(e, lxml.etree._ElementUnicodeResult):
        return unicode(e)
    return None


def parse_lyrics(page):
    """ Parse given page for lyrics contents """
    lyrics = page('div.lyricbox')
    for e in lyrics.contents():
        content = get_lyrics_content(e)
        if content:
            yield content


def get_lyrics(artist, song):
    """ Get lyrics for given song of artist """
    url = get_lyrics_page_url(artist, song)
    resp = requests.get(url)
    page = pq(resp.text)
    return list(parse_lyrics(page))
