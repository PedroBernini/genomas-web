$(document).ready(function() {
    $('#navDatasets').addClass('active-link');
});

function createDataset() {
    var tamanho = $('#tamanho').val();
    var quantidade = $('#quantidade').val();
    var minBkp = $('#min-bkp').val();
    var maxBkp = $('#max-bkp').val();

    if(!tamanho) {
        popWarning('Campo', 'Insira um tamanho')
        $('#tamanho').focus();
        return;
    }

    if(!quantidade) {
        popWarning('Campo', 'Insira a quantidade')
        $('#quantidade').focus();
        return;
    }

    if(!minBkp) {
        popWarning('Campo', 'Insira o mínimo de breakpoints')
        $('#min-bkp').focus();
        return;
    }

    if(!maxBkp) {
        popWarning('Campo', 'Insira o máximo de breakpoints')
        $('#max-bkp').focus();
        return;
    }

    if(isNaN(tamanho)) {
        popWarning('Campo', 'Tamanho precisa ser numérico')
        $('#tamanho').focus();
        return;
    }

    if(isNaN(quantidade)) {
        popWarning('Campo', 'Quantidade precisa ser numérico')
        $('#quantidade').focus();
        return;
    }

    if(isNaN(tamanho)) {
        popWarning('Campo', 'Tamanho precisa ser numérico')
        $('#nome').focus();
        return;
    }

    if(isNaN(minBkp)) {
        popWarning('Campo', 'MIN Breakpoints precisa ser numérico')
        $('#min-bkp').focus();
        return;
    }

    if(isNaN(maxBkp)) {
        popWarning('Campo', 'MAX Breakpoints precisa ser numérico')
        $('#man-bkp').focus();
        return;
    }

    $.ajax({
        type: 'POST',
        url: '/create_dataset/',
        dataType: 'json',
        data: {
            tamanho: tamanho,
            quantidade: quantidade,
            minBkp: minBkp,
            maxBkp: maxBkp
        },
        success: function (data) {
            dataset = data.dataset;
            popSuccess('Create Dataset', data.msg);
            $('#contentDatasets').append(`
                <tr id="dataset_${dataset['id']}">
                    <td>${dataset['nome']}</td>
                    <td>${dataset['tamanho']}</td>
                    <td>${dataset['quantidade']}</td>
                    <td>${dataset['minBkp']}</td>
                    <td>${dataset['maxBkp']}</td>
                    <td><a type="button" data-id="${dataset['id']}" onclick="deleteDataset(this.getAttribute('data-id'))"><i class="fas fa-trash-alt fa-2x text-danger"></i></a></td>
                </tr>
                `);
            hideLoader();
        },
        error: function (data) {
            tratarErro(data);
        }
    });
}

function deleteDataset(idDataset) {
    $.ajax({
        type: 'POST',
        url: '/delete_dataset/',
        dataType: 'json',
        data: {idDataset: idDataset},
        success: function (data) {
            popSuccess('Exclusão', data.msg);
            $('#dataset_' + idDataset).remove();
            hideLoader();
        },
        error: function (data) {
            tratarErro(data);
        }
    });
}