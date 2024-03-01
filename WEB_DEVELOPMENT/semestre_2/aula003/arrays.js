//Arrays

//                0      1    2    3
const numeros = ['Olá', 10, true, {}]
console.log(numeros)

// desestruturação
    //rest
const [saudacao, ...resto] = numeros
    // Spread
const copia = [...numeros]
numeros[1] = 15
console.log(numeros)

 // Array[str]
 let filmes = ['mario', 'maria', 'joana', 'harry', 'potter']
 filmes.push('Senhor')
 filmes.pop()
 filmes.push('Senhora')

 // Array [Object]
let Filmes = [{
    nome: 'harry',
    lançamento: 2001,
    rating: 10
},{
    nome: 'Senhor',
    lançamento: 2004,
    rating: 0
}]


