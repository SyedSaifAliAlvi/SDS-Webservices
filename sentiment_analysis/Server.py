import tornado.web
import tornado.ioloop
from sentiment_analysis_2 import sentiment_Analysis
import asyncio

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('pages/Main_page.html')


class dynamicRequestHandler(tornado.web.RequestHandler):
    def post(self):
        body = self.request.body_arguments
        body = body.get("text")[0].decode('utf-8')
        emotion = sentiment_Analysis(body)
        self.render('pages/result.html', text=body, sentiment=emotion)


if __name__=='__main__':
  app = tornado.web.Application([(r"/",basicRequestHandler),
                                 (r"/result",dynamicRequestHandler)])
  print("API IS RUNNING.......")
  print("http://localhost:8887")
  server = tornado.httpserver.HTTPServer(app)
  server.bind(8887, '127.0.0.1')
  server.start()
  asyncio.get_event_loop().run_forever()