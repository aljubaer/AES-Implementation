

function getInputFileAndCreateTmpFile() {

    const { dialog } = require('electron').remote;
    var fs = require('fs');


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
        
        fs.readFile(result.filePaths[0], 'utf-8', (err, data) => {
            if (err) {
                alert("An error ocurred reading the file :" + err.message);
                return;
            }

            // Change how to handle the file content
            console.log("The file content is : " + data);
            let fn = "text.txt";
            // fileName is a string that contains the path and filename created in the save file dialog.  
            fs.writeFile(fn, data, (err) => {
                if (err) {
                    alert("An error ocurred creating the file " + err.message);
                }

                alert("The file has been succesfully saved");
            });
        });

    }).catch(err => {
        console.log(err);
    });




    // dialog.showOpenDialog((fileNames) => {
    //     // fileNames is an array that contains all the selected
    //     if (fileNames === undefined) {
    //         console.log("No file selected");
    //         return;
    //     }

    //     fs.readFile(filePaths, 'utf-8', (err, data) => {
    //         if (err) {
    //             alert("An error ocurred reading the file :" + err.message);
    //             return;
    //         }

    //         // Change how to handle the file content
    //         console.log("The file content is : " + data);
    //         let fn = "text.txt";
    //         // fileName is a string that contains the path and filename created in the save file dialog.  
    //         fs.writeFile(fn, data, (err) => {
    //             if (err) {
    //                 alert("An error ocurred creating the file " + err.message);
    //             }

    //             alert("The file has been succesfully saved");
    //         });
    //     });
    // });


    // dialog.showOpenDialog({
    //     properties: ['openFile']
    // }).then(result => {
    //     console.log(result.canceled);
    //     console.log(result.filePaths);
    // }).catch(err => {
    //     console.log(err);
    // });
}