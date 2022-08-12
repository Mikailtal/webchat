$(document).ready(function(){
var socket=io.connect("http://localhost:5000")
socket.on('connect',function(){
socket.send("user connected");
});
socket.on('message',function(data){
$('messages').append($('<p>').text(data));
});

$(#sendbtn).on('click',function(){
socket.send($'#username').val()+':'+$('message').val());
$('#message').val('')
})
})