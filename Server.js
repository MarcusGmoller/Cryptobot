const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const WebSocket = require('ws');
const { sign } = require('jsonwebtoken');
const crypto = require('crypto');

// Dine eksisterende WebSocket og JWT signering funktioner her

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

// Serve en simpel HTML-fil til klienten
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Opret WebSocket-forbindelse til Coinbase eller en anden service
const ws = new WebSocket('wss://advanced-trade-ws.coinbase.com');

ws.on('open', function open() {
  // Send din abonnementsanmodning her
});

ws.on('message', function incoming(data) {
    console.log('Data received from WebSocket:', data); // Tilføj denne linje for at logge data
    io.emit('data', data.toString()); // Sørg for at konvertere Buffer til en streng, hvis nødvendigt
  });
  

// Opsæt Socket.IO til at lytte på 'connection' event
io.on('connection', (socket) => {
  console.log('A user connected');
  socket.on('disconnect', () => {
    console.log('User disconnected');
  });
});

// Lyt på port 3000
server.listen(3000, () => {
  console.log('Listening on *:3000');
});
