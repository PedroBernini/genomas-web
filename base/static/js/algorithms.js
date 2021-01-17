$(document).ready(function() {
    $('#navAlgorithms').addClass('active-link');
});

function createDatasetTxt() {

    var idDataset = $('#datasetSelect').val();

    if(!idDataset) {
        popWarning('Campo', 'Selecione um dataset!')
        $('#datasetSelect').focus();
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/create_dataset_txt/',
        dataType: 'json',
        data: {idDataset: idDataset},
        success: function (data) {
            popSuccess('Criação de Dataset', data.msg);
            hideLoader();
        },
        error: function (data) {
            tratarErro(data);
        }
    });
}

function kececiogluAlgorithm() {
    
    var idDataset = $('#datasetSelect').val();

    if(!idDataset) {
        popWarning('Campo', 'Selecione um dataset!')
        $('#datasetSelect').focus();
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/kececioglu_algorithm/',
        dataType: 'json',
        data: {idDataset: idDataset},
        success: function (data) {
            popSuccess('Algoritmo', data.msg);
            hideLoader();
        },
        error: function (data) {
            tratarErro(data);
        }
    });
}

function reinforcementAlgorithm() {
    var idDataset = $('#datasetSelect').val();
    var modelo = $('#modeloSelect').val();

    if(!idDataset) {
        popWarning('Campo', 'Selecione um dataset!')
        $('#datasetSelect').focus();
        return;
    }

    if(!modelo) {
        popWarning('Campo', 'Selecione um modelo!')
        $('#modeloSelect').focus();
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/reinforcement_algorithm/',
        dataType: 'json',
        data: {
            idDataset: idDataset,
            modelo: modelo
        },
        success: function (data) {
            if(data.info) {
                popWarning('Reinforcement Learning', data.info);
            } else {
                popSuccess('Reinforcement Learning', data.msg);
            }
            hideLoader();
        },
        error: function (data) {
            tratarErro(data);
        }
    });
}