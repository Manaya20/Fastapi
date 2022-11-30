const express = require('express');
const http = require('http');

const app = express();
const router = express.Router();

router.use((req, res, next) => {
  res.header('Access-Control-Allow-Methods', 'GET');
  next();
});

router.get('/healthcheck', (req, res) => {
  res.status(200).send('Ok');
});

app.use('/api/v1', router);

const server = http.createServer(app);
server.listen(3000);