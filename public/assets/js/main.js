const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


// Message FadeOut ~ 3 Seconds;
setTimeout(function() {
    $('#ErrorMessages').fadeOut('slow');
}, 3000);           