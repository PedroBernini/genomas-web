$(document).ready(function() {
    ajaxConfig()
});

function ajaxConfig() {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function gerarNovaRede() {
    

    $.ajax({
        type: 'POST',
        url: '/gerar_nova_rede/',
        dataType: 'json',
        data: {},
        success: function (data) {
            alert(data.msg)
        },
        error: function (data) {
            
        }
    });
}