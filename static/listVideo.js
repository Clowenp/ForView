window.onload = function() {
    fetch('/getUserData')
    .then((res)=>{ console.log(res)});
}