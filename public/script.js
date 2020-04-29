var inp = document.getElementById('input-file');
var textinp = document.getElementById('text-input-file');

inp.onchange = function (e) {
    var file = this.files[0].name;
    textinp.innerText = file;
}
