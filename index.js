var formidable = require('formidable');
const express = require('express');
const app = express();
var spawn = require('child_process').spawn;
app.listen(3000);

app.post('/fileupload', (req, res) => {
    var form = new formidable.IncomingForm();
    form.parse(req, function (err, fields, files) {
        var name = fields.name;
        var number = fields.number;
        var file = files.filetoupload.path;
        var process = spawn('python', ["./script.py", file, name, number]);
        process.on('exit', code => {
            res.download(file, "sms.json");
        });
    });
});

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
    app.use(express.static(__dirname + '/public'));
    app.use('/css', express.static(__dirname + '/node_modules/bootstrap/dist/css'));
});
