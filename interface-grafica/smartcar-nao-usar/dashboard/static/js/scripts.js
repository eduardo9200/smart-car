console.log('olá, mundo!');

function validar() {
    var ip = formularioIp.ipNumber.value;
console.log(ip)
    $('#frame-camera').src = 'http://' + ip + ':8000';
}

function acao() {
    console.log('faça algo')
}