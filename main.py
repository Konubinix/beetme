#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import os
import mimetypes
import requests
import sys
import tempfile
from urllib import parse

from flexx import app, config
import tornado

from beetme import BeetMe

logging.basicConfig(level=logging.INFO)

config.hostname = "0.0.0.0"
config.port = 9665
config.tornado_debug = True


class BeetHandler(tornado.web.RequestHandler):
    def get(self):
        uri = self.request.uri[5:]
        self.write(requests.get("http://192.168.2.2:8337" + uri).content)


def main():
   if len(sys.argv) > 1:
        app.export(BeetMe, "beetme.html", link=0)
   else:
       app.serve(BeetMe)
       tornado_app = app.current_server().app
       tornado_app.add_handlers(
           r".*", [
               (r"/beet.*", BeetHandler),
           ]
       )
       app.start()


if __name__ == "__main__":
    main()
