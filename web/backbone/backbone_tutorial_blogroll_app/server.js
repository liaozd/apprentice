var express = require('express');
var mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/blogroll');

var Schema = mongoose.Schema;

var BlogSchema = new Schema({
  author: String,
  title: String,
  url: String
});

mongoose.model('Blog', BlogSchema);

var Blog = mongoose.model('Blog');

var blog = new Blog({
  author: 'Mi',
  title: 'Title',
  url: 'http:'
});

blog.save();

var app = express();


// ROUTES

app.get('/api/blogs', function (req, res) {
  Blog.find(function (err, docs) {
    docs.forEach(function (item) {
      console.log('Received a GET request for _id: ' + item._id);
    });
    res.send(docs);
  })
});

app.use(express.static(__dirname + '/public'));

var port = 3000;

app.listen(port);
console.log('server on ' + port);
