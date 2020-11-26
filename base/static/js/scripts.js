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

function atualizarPoliticas() {

    $.ajax({
        type: 'POST',
        url: '/atualizar_politicas/',
        dataType: 'json',
        data: {},
        success: function (data) {
            document.getElementById("policy_123").className = data.politicas['[1, 2, 3]'];
            document.getElementById("policy_213").className = data.politicas['[2, 1, 3]'];
            document.getElementById("policy_231").className = data.politicas['[2, 3, 1]'];
            document.getElementById("policy_132").className = data.politicas['[1, 3, 2]'];
            document.getElementById("policy_312").className = data.politicas['[3, 1, 2]'];
            document.getElementById("policy_321").className = data.politicas['[3, 2, 1]'];
            alert(data.msg)
        },
        error: function (data) {
            
        }
    });
}

function treinarRede() {
    epochs = document.getElementById("epoch").value
    $.ajax({
        type: 'POST',
        url: '/treinar_rede/',
        dataType: 'json',
        data: {'epochs': epochs},
        success: function (data) {
            alert(data.msg)
        },
        error: function (data) {
            
        }
    });
}