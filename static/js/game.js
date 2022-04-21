
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/game');
    socket.on('test', function(msg) {
        console.log('Received: ' + JSON.stringify(msg));
    });
    
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
});