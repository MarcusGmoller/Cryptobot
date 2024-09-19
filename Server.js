const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const WebSocket = require('ws');
const { sign } = require('jsonwebtoken');
const crypto = require('crypto');

// eksisterende WebSocket og JWT signering funktioner

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

// Serve en simpel HTML-fil til klienten
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Opret WebSocket-forbindelse til Coinbase
const ws = new WebSocket('wss://advanced-trade-ws.coinbase.com');

ws.on('open', function open() {
  // Send din abonnementsanmodning her
});

ws.on('message', function incoming(data) {
    console.log('Data received from WebSocket:', data); // logger data
    io.emit('data', data.toString()); // konvertere Buffer til en streng, hvis nødvendigt
  });
  

// Opsæt Socket.IO til at lytte på 'connection' event
io.on('connection', (socket) => {
  console.log('A user connected');
  socket.on('disconnect', () => {
    console.log('User disconnected');
  });
});

server.listen(3000, () => {
  console.log('Listening on *:3000');
});
