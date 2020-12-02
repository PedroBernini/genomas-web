$(document).ready(function() {
    
});

//Loader
function showLoader() {
    $('body').removeClass('loaded');
    $('#loader-wrapper').show();
}

function hideLoader() {
    $('#loader-wrapper').hide();
}

function hideLoaderWithEffect() {
    $('body').addClass('loaded');
}