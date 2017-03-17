from tornado import websocket, web, ioloop
import MySQLdb

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print "Connection Established"

    def on_message(self, message):
        #our query string 
        query = "INSERT INTO test(number) VALUES (" + message + ")"
        #execute SQL query using execute() method.
        cursor.execute(query)
        db.commit()

    def on_close(self):
        # disconnect from mysql server
        db.close()
        print "Connection Closed"

app = web.Application([(r'/ws', SocketHandler)])

if __name__ == '__main__':
    # Open database connection
    db = MySQLdb.connect("localhost","newuser","password","testing" )
    cursor = db.cursor()
    #listen for requests on port 8888 
    app.listen(8888)
    ioloop.IOLoop.instance().start()


