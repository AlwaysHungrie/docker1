var express = require('express');
var fs = require("fs");
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.json({ type: 'application/*+json' }));
app.use(bodyParser.urlencoded({extended: true}));
// parse some custom thing into a Buffer
app.use(bodyParser.raw({ type: 'application/vnd.custom-type' }));

// parse an HTML body into a string
app.use(bodyParser.text({ type: 'text/html' }));

app.listen(8080);
app.get('/',(req,res)=>{
        res.sendFile(__dirname+'/index.html');
});
app.get('/persistant',(re,rs)=>{
        rs.sendFile(__dirname+"/data/temp.txt");
});
app.post('/action',(req,res)=>{
var data =req.body.firstname+ " " + req.body.lastname;
console.log(req.body);
console.log(req.body.firstname);
fs.writeFile("data/temp.txt", data, (err) => {
  if (err) console.log(err);
  console.log("Successfully Written to File.");
  res.sendFile(__dirname+'/index.html');
});
});
