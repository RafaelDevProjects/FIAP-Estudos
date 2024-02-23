const $divListaFilmes = document.querySelector('#listaFilmes');
const btn1 = document.querySelector('button')
const $filmeInput = document.querySelector('#filmeInput')
const titulo = document.querySelector('h1')

const $itemLista = document.createElement('li');
btn1.addEventListener('click', () =>{
    //adiciona a lista
    $divListaFilmes.append($itemLista);
    //adiciona texto dinamico ao elemento
    $itemLista.innerHTML = $filmeInput.value
    titulo.innerHTML($itemLista)

})