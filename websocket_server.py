from tornado import websocket, web, ioloop

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print "Connection Established"

    def on_message(self, message):
        print "Message received"
        self.write_message(u"You said: %s" % message)

    def on_close(self):
        print "Connection Closed"

app = web.Application([(r'/ws', SocketHandler)])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()


