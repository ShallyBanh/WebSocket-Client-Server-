import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import MySQLdb


class SimpleHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.getheader('content-length'))        
        message = self.rfile.read(length)
        #our query string 
        query = "INSERT INTO http(id) VALUES (" + message + ")"
        #execute SQL query using execute() method.
        cursor.execute(query)
        db.commit()

def start_server():
    """Start the server."""
    serverAddress = ("", 8883)
    server = BaseHTTPServer.HTTPServer(serverAddress, SimpleHandler)
    server.serve_forever()

if __name__ == "__main__":
    # Open database connection
    db = MySQLdb.connect("localhost","newuser","password","testing" )
    cursor = db.cursor()
    start_server()