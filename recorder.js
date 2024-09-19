let blobs = [];
let stream;
let rec;
let recordUrl;
let audioResponseHandler;

function recorder(url, handler) {
    recordUrl = url;
    if (typeof handler != "undefined") {
        audioResponseHandler = handler;
    }
}

async function record() {
    
}