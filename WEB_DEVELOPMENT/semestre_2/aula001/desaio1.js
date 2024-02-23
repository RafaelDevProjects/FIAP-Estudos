function qntLivros(){
    let quantidadelivros = 4

    return quantidadelivros
}

function calcPreco(livros = qntLivros()){
    let preco = 22

    if (livros >= 7){
        preco = 15
    }

    return preco * livros
}

function main(){
    console.log(calcPreco())
}

main()
    




