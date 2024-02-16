function getUserInfo(){
    velocidade = 61
    return velocidade
}

function valorMulta(velocidade = getUserInfo()){
    if (velocidade > 60){
        subtracao = velocidade - 60
        multa = subtracao * 100
        return multa
    }else {
        return multa
    }
}


function main(){
    console.log(valorMulta())


}

main()