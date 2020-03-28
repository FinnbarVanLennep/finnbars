console.log("pongController.js loaded.")

const threshhold = 150;
const moveDisplacement = -10;

function rotationHandler(rotation) {
    let rotText = document.getElementById("dir");

    if (Math.abs(rotation.gamma) > threshhold) {
        rotText.innerHTML = (rotation.gamma < 0) ? "UP" : "DOWN";
        socket.emit('move', Math.sign(rotation.gamma) * moveDisplacement);
    } else {
        rotText.innerHTML = "-";
    }
}

var socket = io('http://192.168.1.225:5000/pong');
socket.on('connect', function(){
    console.log("Websocket connected!");
});
socket.on('move', function(data){
    console.log(`socket 'move': ${data}`);
});
socket.on('disconnect', function(){
    console.log("Websocket disconnected...");
});


if ('Gyroscope' in window) {
    console.log('using: Generic Sensor API');
    
    let gyroscope = new Gyroscope();
    gyroscope.addEventListener('reading', e => rotationHandler({
        alpha: gyroscope.x,
        beta: gyroscope.y,
        gamma: gyroscope.z
    }));
    gyroscope.start();

} else if ('DeviceMotionEvent' in window) {
    console.log('using: Device Motion API');
    
    let updateCounter = 0;
    const updateRate = 5;   // Updates per second
    window.addEventListener('devicemotion', eventData => {

        if (updateCounter * updateRate >= eventData.interval) {
            rotationHandler(eventData.rotationRate);
            updateCounter = 0;
        }
        updateCounter += 1;

    }, false);
    
} else {
    document.getElementById('moApi').innerHTML = 'No Gyroscope API available';
}