$(document).ready(function() {
    $('#navTraining').addClass('active-link');
});

function createNetwork() {
    var tamanhoRede = $('#tamanhoRede').val();
    var epocas = $('#epocas').val();
    var optimizer = $('#optimizer').val();
    var lossFunction = $('#lossFunction').val();

    if(!tamanhoRede) {
        popWarning('Campo', 'Insira um tamanho da rede')
        $('#tamanhoRede').focus();
        return;
    }

    if(!epocas) {
        popWarning('Campo', 'Insira a quantidade de épocas')
        $('#epocas').focus();
        return;
    }

    if(isNaN(tamanhoRede)) {
        popWarning('Campo', 'Tamanho da rede precisa ser numérico')
        $('#tamanhoRede').focus();
        return;
    }

    if(isNaN(epocas)) {
        popWarning('Campo', 'Quantidade de épocas precisa ser numérico')
        $('#epocas').focus();
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/create_network/',
        dataType: 'json',
        data: {
            tamanhoRede: tamanhoRede,
            epocas: epocas,
            optimizer: optimizer,
            lossFunction: lossFunction
        },
        success: function (data) {
            popSuccess('Criação de Rede', data.msg);
            hideLoader();
        },
        error: function (data) {
            tratarErro(data);
        }
    });
}