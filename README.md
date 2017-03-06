# WebSocket-Client-Server

Websockets are a bidirectional, single-socket connection. With WebSocket, your HTTP request becomes a single request to open a WebSocket connection and reuses the same connection between client and server. Also, WebSocket reduces latency. For example, unlike polling, WebSocket makes a single request. The server does not need to wait for a request from the client. Similarly, the client can send messages to the server at any time. Currently the code above just shows the basics of websockets (establishing a connection, sending a message from the client to server and back, and closing the connection). There is much more that you can with websockets but this is just a small demo of the basics of websockets.

#Usage

In your terminal run:

python websocket_server.py

Then open up the websocket.html in google chrome or whatever browser you're using. You should be able to see the websockets connecting either through the terminal window (server side) or you can open up dev tools on your browser window and you can see it from there (client side). Currently the server will echo back the whole message and the header also. 

