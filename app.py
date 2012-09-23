#!/usr/bin/env python

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from settings import settings
from urls import url_patterns

class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
    	settings = {
    		'static_path'   : "static",
            'template_path' : "templates",
		}
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = TornadoBoilerplate()
    http_server = tornado.httpserver.HTTPServer(app)
    options.port = "8080"
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
