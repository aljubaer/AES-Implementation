var fs = require('fs');
var ps = require("python-shell");
var path = require("path");

var inputProperticsEncrytion = {
    message: "Self respect is something that you should never lose",
    key: "tahmid khan",
    keylen: "32",
    outputFile: "aes.bin",
    aes_mode: "cFB",
    iv: "tahmid"
};

var inputProperticsDecrytion = {
    key: inputProperticsEncrytion.key,
    keylen: inputProperticsEncrytion.keylen,
    outputFile: "aes.txt",
    aes_mode: inputProperticsEncrytion.aes_mode,
    iv: inputProperticsEncrytion.iv
};


function getInputFileForEncrypt() {

    const { dialog } = require('electron').remote;

    let fileContent = '';


    dialog.showOpenDialog({
        properties: ['openFile']
    }).then(result => {
        console.log(result.canceled);
        console.log(result.filePaths);

        if (result.filePaths.length == 0)
            return;

        console.log('not cancelled');

        console.log(result.filePaths[0]);
        document.getElementById("enFileInput").value = result.filePaths[0];

        fs.readFile(result.filePaths[0], 'utf-8', (err, data) => {
            if (err) {
                alert("An error ocurred reading the file :" + err.message);
                return;
            }

            console.log("The file content is : " + data);
            inputProperticsEncrytion.message = data;
            document.getElementById('enInputString').value = data;
        });

    }).catch(err => {
        console.log(err);
    });
}

function onEncryptHandler() {
    var me = document.getElementById("mode");
    inputProperticsEncrytion.aes_mode = me.options[me.selectedIndex].text;
    var ke = document.getElementById("keysize");
    inputProperticsEncrytion.keylen = ke.options[ke.selectedIndex].text;
    inputProperticsEncrytion.iv = document.getElementById("encryptivinput").value;
    inputProperticsEncrytion.key = document.getElementById("secretkey").value;
    console.log(inputProperticsEncrytion);

    let fn = "en_input.json";
    fs.writeFile(fn, JSON.stringify(inputProperticsEncrytion), (err) => {
        if (err) {
            alert("An error ocurred creating the file " + err.message);
        }

        var options = {
            scriptPath: path.join(__dirname, '/../engine/')
        };

        ps.PythonShell.run('aes_encrypt.py', options, function (err, results) {
            if (err) throw err;
            console.log('results: %j', results);
            fs.readFile('encrypt.bin', 'utf-8', (err, data) => {
                if (err) {
                    alert("An error ocurred reading the file :" + err.message);
                    return;
                }

                console.log("The file content is : " + data);
                document.getElementById('outputString').value = data;
            });
        });
    });
}


function getInputFileForDecrypt() {

    const { dialog } = require('electron').remote;

    let fileContent = '';


    dialog.showOpenDialog({
        properties: ['openFile']
    }).then(result => {
        console.log(result.canceled);
        console.log(result.filePaths);

        if (result.filePaths.length == 0)
            return;

        console.log('not cancelled');

        console.log(result.filePaths[0]);
        document.getElementById("deFileInput").value = result.filePaths[0];

        fs.readFile(result.filePaths[0], (err, data) => {
            if (err) {
                alert("An error ocurred reading the file :" + err.message);
                return;
            }

            console.log("The file content is : " + data);
            document.getElementById('dinputString').value = data;
            let fn = "aes_tmp.bin";
            fs.writeFile(fn, data, (err) => {
                if (err) {
                    alert("An error ocurred creating the file " + err.message);
                }
            });

        });

    }).catch(err => {
        console.log(err);
    });
}


function onDecryptHandler() {
    var me = document.getElementById("dmode");
    inputProperticsDecrytion.aes_mode = me.options[me.selectedIndex].text;
    var ke = document.getElementById("dkeysize");
    inputProperticsDecrytion.keylen = ke.options[ke.selectedIndex].text;
    inputProperticsDecrytion.iv = document.getElementById("decryptivinput").value;
    inputProperticsDecrytion.key = document.getElementById("dsecretkey").value;
    console.log(inputProperticsDecrytion);

    let fn = "de_input.json";
    fs.writeFile(fn, JSON.stringify(inputProperticsDecrytion), (err) => {
        if (err) {
            alert("An error ocurred creating the file " + err.message);
        }

        var options = {
            scriptPath: path.join(__dirname, '/../engine/')
        };

        ps.PythonShell.run('aes_decrypt.py', options, function (err, results) {
            if (err) throw err;
            console.log('results: %j', results);
            fs.readFile('decrypt.txt', 'utf-8', (err, data) => {
                if (err) {
                    alert("An error ocurred reading the file :" + err.message);
                    return;
                }

                console.log("The file content is : " + data);
                document.getElementById('doutputString').value = data;
            });
        });
    });
}