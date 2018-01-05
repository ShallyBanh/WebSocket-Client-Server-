# WebSocket-Client-Server

Websockets are a bidirectional, single-socket connection. With WebSocket, your HTTP request becomes a single request to open a WebSocket connection and reuses the same connection between client and server. Also, WebSocket reduces latency. For example, unlike polling, WebSocket makes a single request. The server does not need to wait for a request from the client. Similarly, the client can send messages to the server at any time.

# Implementation 
In order to show "why use websockets?", the code above shows how long it will take to use a Websocket protocol to process 100 requests from the client to server vs how long it would take to use a HTTP protocol to process 100 requests from the client to server. In each request the client sends a request to the server to insert a number into a database. This is done because i wanted the client/server to being doing something more pratical than just establishing a connection between the two and printing out to the standard output that it is indeed working as expected. I wanted some actual data to be transfered.

Anyways in order for the code to run, i created a new random database called "testing" and then in the database i created two tables called "test" (for websocket protocol) and "http" (for http protocol) and a new user called "newuser" who has access to the "test" database. 

# Usage

In order to run the tests using the websocket protocol, in the terminal run:

```
python websocket_server.py
```

Then open up the websocket.html in google chrome or whatever browser you're using. You should be able to see the websockets connecting either through the terminal window (server side) or you can open up dev tools on your browser window and you can see it from there (client side). You should also see on the client side the time it took to process the 100 requests. you can also open up your table in your database and check that there are indeed 100 new entries written into it. 

In order to run the tests using the HTTP protocol, do the same as you did for the websocket expect using Http.py and httpExample.html

# Discussion
From running the code/test, I found that for the Websocket protocol it took 10.607ms to process the 100 requests. For the Http protocol i found that it took 265.654ms. As you can see it is way faster to use websockets because in websockets it only sends http in the header once (to establish a handshake between client and server) but for http protocol it sends http in the header each time a request is made.

# Future TO DOs
Not quite sure yet

