function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {

        showLoader();
        
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function tratarErro(data) {
    if(data.statusText == "error") {
        popError('Erro de conexão', 'Verifique a conexão da sua internet!');
        hideLoaderWithEffect();
        return
    }

    if(data.statusText == "INTERNAL SERVER ERROR") {
        popError('Erro interno', 'Um erro interno ocorreu no servidor!');
        hideLoaderWithEffect();
        return
    }

    try {
        popError('Erro', data.responseJSON.msg)
    } catch {
        popError('Erro', 'Erro de resposta no servidor')
    } finally {
        hideLoaderWithEffect();
    }
}