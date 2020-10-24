const BASE_URL = 'http://localhost:8000/api/v1/';


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {  // нормальный ответ
        return await response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function onAdd(event) {
    event.preventDefault();
    let addBtn = event.target;
    let url = addBtn.href;
    console.log(url);
    try {
        let response = await makeRequest(url, 'POST');
        console.log(response);

    }
    catch (error) {
        console.log(error);
    }

    addBtn.classList.add('hidden');
    const deleteBtn = addBtn.parentElement
        .getElementsByClassName('delete')[0];
    deleteBtn.classList.remove('hidden');
}

async function onDelete(event) {
    event.preventDefault();
    let deleteBtn = event.target;
    let url = deleteBtn.href;

    try {
        let response = await makeRequest(url , "DELETE");
        console.log(response);

    }
    catch (error) {
        console.log(error);
    }

    deleteBtn.classList.add('hidden');
    const addBtn = deleteBtn.parentElement
        .getElementsByClassName('add')[0];
   addBtn.classList.remove('hidden');
}

window.addEventListener('load', function() {
    const addButtons = document.getElementsByClassName('add');
    const deleteButtons = document.getElementsByClassName('delete');

    for (let btn of addButtons) {btn.onclick = onAdd}
    for (let btn of deleteButtons) {btn.onclick = onDelete}
});