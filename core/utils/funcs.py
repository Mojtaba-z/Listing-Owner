# requests functions
from urllib.request import urlopen

import requests
from requests import request

import logging

log = logging.getLogger(__name__)


def get_request(url, params=None): return requests.get(url=url, params=params, )


def post_request(url, params=None, key=None): return requests.post(url=url, params=params)


def put_request(url, params=None, key=None): return requests.put(url=url, params=params)


def delete_request(url, params=None, key=None): return requests.delete(url=url, params=params)


def get_request_headers(r: requests): return r.headers


def get_request_content(r: requests): return r.content


def get_request_url(r: requests): return r.url


def get_request_json(r: requests): return r.json()


def get_request_text(r: requests): return r.text


def get_request_token(r: requests): return get_request_json(r)['headers']['Authorization']


def get_request_user_agent(r: requests): return get_request_json(r)['headers']['User-Agent']


def get_request_host(r: requests): return get_request_json(r)['headers']['Host']

