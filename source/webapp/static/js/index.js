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

async function add(event) {
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
    console.log(addBtn)
    addBtn.style.display="none"
    console.log(addBtn.id)
    const delBtn = addBtn.parentElement.getElementsByClassName('remove')[0];
    console.log(delBtn)
    delBtn.style.display="block"
}

async function remove(event) {
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
    deleteBtn.style.display="none"
    const add_Btn = deleteBtn.parentElement.getElementsByClassName('add')[0];
    add_Btn.style.display="block"
}

window.addEventListener('load', function() {
    const addButtons = document.getElementsByClassName('add');
    const removeButtons = document.getElementsByClassName('remove');
    console.log(addButtons)
    for (let btn of addButtons) {btn.onclick = add}
    for (let btn of removeButtons) {btn.onclick = remove}
});



// async function makeRequest(url, method='GET') {
//     console.log(method)
//     let response = await fetch(url, {method});
//
//     if (response.ok) {  // нормальный ответ
//         return await response.text();
//     } else {            // ошибка
//         let error = new Error(response.statusText);
//         error.response = response;
//         throw error;
//     }
// }
//
// async function add(event) {
//     event.preventDefault();
//     let addBtn = event.target;
//     let url = addBtn.href;
//     console.log(url)
//     try {
//         let response = await makeRequest(url, 'POST');
//         console.log(response);
//         // const counter = likeBtn.parentElement
//         //     .getElementsByClassName('counter')[0];
//         // counter.innerText = response;
//     }
//     catch (error) {
//         console.log(error);
//     }
//
//     // likeBtn.classList.add('hidden');
//     // const unlikeBtn = likeBtn.parentElement
//     //     .getElementsByClassName('unlike')[0];
//     // unlikeBtn.classList.remove('hidden');
// }
//
// async function remove(event) {
//     event.preventDefault();
//     let unLikeBtn = event.target;
//     let url = unLikeBtn.href;
//
//     try {
//         let response = await makeRequest(url, 'DELETE');
//         console.log(response);
//         // const counter = unLikeBtn.parentElement
//         //     .getElementsByClassName('counter')[0];
//         // counter.innerText = response;
//     }
//     catch (error) {
//         console.log(error);
//     }
//
//     // unLikeBtn.classList.add('hidden');
//     // const likeBtn = unLikeBtn.parentElement
//     //     .getElementsByClassName('like')[0];
//     // likeBtn.classList.remove('hidden');
// }
//
// window.addEventListener('load', function() {
//     const addButtons = document.getElementsByClassName('add');
//     const removeButtons = document.getElementsByClassName('remove');
//     console.log(addButtons)
//     for (let btn of addButtons) {btn.onclick = add}
//     for (let btn of removeButtons) {btn.onclick = remove}
// });