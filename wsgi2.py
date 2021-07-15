#!/usr/local/bin/python3

import re
from html import escape

def index(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    response = ['index called']
    return (line.encode('utf-8') for line in response)

def hello(environ, start_response):
    args = environ['url_args']
    if args:
        name = args[0]
    else:
        name = 'world'
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    response = ['Hello {}'.format(name)]
    return (line.encode('utf-8') for line in response)

def not_found(environ, start_response):
    start_response('404 NOT FOUND', [('Content-Type',
                                      'text/plain;charset=utf-8')]
    response = ['Not Found']
    return (line.encode('utf-8') for line in response

urls = [
    (r'^$', index),
    (r'hello/?$', hello),
    (r'hello/(.+)$', hello)
]

def application(environ, start_response):
    path = environ.get('PATH_INFO', '').lstrip('/')
    for regex, callback in urls:
        match = re.search(regex, path)
        if match:
            environ['url_agrs'] = match.groups()
            return callback(environ, start_response)
    return not_found(environ, start_response)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('python.kw.ac.kr', 8080, application)
    srv.serve_forever()
