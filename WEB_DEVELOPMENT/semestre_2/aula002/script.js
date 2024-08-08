// const $divListaFilmes = document.querySelector('#listaFilmes');
// const btn1 = document.querySelector('button')
// const $filmeInput = document.querySelector('#filmeInput')
// const titulo = document.querySelector('h1')

// const $itemLista = document.createElement('li');
// btn1.addEventListener('click', () =>{
//     //adiciona a lista
//     $divListaFilmes.append($itemLista);
//     //adiciona texto dinamico ao elemento
//     $itemLista.innerHTML = $filmeInput.value
//     titulo.innerHTML($itemLista)

// })

const listaFilmes = document.querySelector("#listaFilmes")
// // com strings
 let filmes = ['mario', 'maria', 'joana', 'harry', 'potter']
 filmes.push('Senhor')
 filmes.pop()
 filmes.push('Senhora')

//   // Array [Object]
// let Filmes = [{
//     nome: 'harry',
//     lançamento: 2001,
//     rating: 10
// },{
//     nome: 'Senhor',
//     lançamento: 2004,
//     rating: 0
// }]

window.onload = () => {
    for(let i = 0; i < filmes.length; i++){
        let listaItem = document.createElement('li')
        listaFilmes.append(listaItem)
        listaItem.innerHTML = filmes[i]
    }
}