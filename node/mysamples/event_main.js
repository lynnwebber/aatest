var events = require('events');
var emitter = new events.EventEmitter();

var connectionHandler = function connected() {
    console.log('connection made');
    emitter.emit('got_connection')
}

function sleep(time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}

emitter.on('start',connectionHandler);

emitter.on('got_connection', function(){
    sleep(50).then(() => {
        console.log('connectionHandler->(emit)got_connection->did_something_1')
    });
});

emitter.on('got_connection', function(){
    console.log('connectionHandler->(emit)got_connection->did_something_2')
});

emitter.emit("start");

console.log("program end.");
