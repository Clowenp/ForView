/*
TIMER CODE
*/
var time = 0;
function timer() {
    document.getElementById("timer").innerText = Math.floor(time/60) + " m " + (time%60).toString() + " s";
    time = time + 1;
}

function getFileName() {
    const date = new Date();
    return (date.getMonth()+1).toString().padStart(2, 0) + "-" +
            date.getDate().toString().padStart(2, 0) + "-" +
            date.getHours().toString().padStart(2, 0) + "-" +
            date.getMinutes().toString().padStart(2, 0) + "-" +
            date.getSeconds().toString().padStart(2, 0);
}


/*
Camera Code
*/
var button = document.getElementById("record_button");
var isRecording = button.innerText == "RECORD" ? false : true;
var t;
const frames = [];

window.onload = function() {
    navigator.mediaDevices.getUserMedia({ audio: true, video: true} ).then(stream => {
        document.getElementById("video").srcObject = stream;
        button.onclick = function() {
            if (button.innerText == "RECORD"){
                isRecording = true;
                t = setInterval(timer, 1000);
                button.innerText = "STOP"
        
                mediaRecorder = new MediaRecorder(stream);
                mediaRecorder.start(1000);
                mediaRecorder.ondataavailable = function (e) {
                    frames.push(e.data);
                }
        
            }
            else{
                button.innerText="RECORD";
                isRecording = false;
                clearInterval(t);
                mediaRecorder.stop();
                const blob = new Blob(frames, {type: "video/mp4"});
                const url = URL.createObjectURL(blob);
                var data = new FormData();
                var filename = getFileName() + ".mp4";

                data.append('file', blob, filename);

                fetch('http://localhost:5000/receive', {
                    method: "POST",
                    body: data
                })
                .catch(err => alert(err));

                var jsonTag = new Object();
                jsonTag.FILENAME = filename;
                jsonTag.ID = Math.floor(Math.random() * 100);
                jsonTag.SCORE = Math.floor(Math.random() * 100);
                var stringJSON = JSON.stringify(jsonTag);

                fetch('http://localhost:5000/update ', {
                    method: "POST",
                    body: stringJSON
                })
                .catch(err => alert(err));
            }
        }
    })
}

