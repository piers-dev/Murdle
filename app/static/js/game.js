
$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/game');
    socket.on('updatestate', function(msg) {
        console.log('Received: ' + JSON.stringify(msg));
        rendergame(msg['state']);
    });
    
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
});