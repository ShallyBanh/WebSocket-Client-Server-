# WebSocket-Client-Server

Websockets are a bidirectional, single-socket connection. With WebSocket, your HTTP request becomes a single request to open a WebSocket connection and reuses the same connection between client and server. Also, WebSocket reduces latency. For example, unlike polling, WebSocket makes a single request. The server does not need to wait for a request from the client. Similarly, the client can send messages to the server at any time.

# Implementation 
In order to show "why use websockets?", the code above measures how long it will take for the websocket client/server to process 10000 requests from the client to the server. But clearly it would be lame if all i did was send a request to server and print out the message because no one would have any actual use for that. So to make this a bit more of a realistic example, the websocket client will send a number to the server and the server will process this number and insert it into a new row of a column of a database. This is more of a practical usage since we're actually doing something and not just printing out to the screen. 

Anyways in the code, i just created a new random database called "test" and then in the database i create a table called "testing" and a new user who has access to the "test" database so we can make a query. Note: it's not really important how you name your database or table just as long as you create one before you run the code or else we cannot make a query to it if there's nothing to query to. 

# Usage

In your terminal run:

python websocket_server.py

Then open up the websocket.html in google chrome or whatever browser you're using. You should be able to see the websockets connecting either through the terminal window (server side) or you can open up dev tools on your browser window and you can see it from there (client side). You should also see on the client side the time it took to process the 10000 requests. you can also open up your table in your database and check that there are indeed 10000 new entries written into it. 

# Dicussion
From running the code/test, I found that it took 317.579ms to process the 10000 requests and to insert 10000 new rows into a database. This has no signifigant meaning right now since there is nothing to compare it to yet for now....

# Future TO DOs
Create the same thing but using ajax and do a comparision in the time it takes to complete the 10000 requests. Websockets should be faster since there is less overhead in the header since we only have to send it once in the handshake initiation. 

