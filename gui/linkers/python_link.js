var ps = require("python-shell");
var path = require("path");

function getSimpleResponse() {


    var inputMessage = "This is a test input";
    inputMessage = document.getElementById("plainTextMessage").value;
    console.log(inputMessage);
    var key = document.getElementById("plainKey").value;

    var options = {
        scriptPath: path.join(__dirname, '/../engine/'),
        args: [inputMessage, key]
    };

    var res = ps.PythonShell.run('python-engine.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
        document.getElementById("responseText").innerHTML = "The response here ->\n " + results;
        return results;
    });

    res.on('message', function (message) {
        //swal(message);
        console.log(message);
        document.getElementById("responseText").value = "The response here -> " + message;
    });
}

module.exports.encryptLink = function encryptionHandler() {
    var options = {
        scriptPath: path.join(__dirname, '/../engine/')
    };

    ps.PythonShell.run('python-engine.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });

};


function decryptionHandler() {
    var options = {
        scriptPath: path.join(__dirname, '/../engine/')
    };

    ps.PythonShell.run('aes_decrypt.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
    });

}