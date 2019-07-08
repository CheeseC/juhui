const http = require('http')

function getClientIp(req) {
  return req.headers['x-forwarded-for'] || // 判断是否有反向代理 IP
    req.connection.remoteAddress || // 判断 connection 的远程 IP
    req.socket.remoteAddress || // 判断后端的 socket 的 IP
    req.connection.socket.remoteAddress;
}

http.createServer(function (request, response) {
  console.log('================================')
  console.log(getClientIp(request))
  response.end('Hello World\n');
}).listen(8888)

