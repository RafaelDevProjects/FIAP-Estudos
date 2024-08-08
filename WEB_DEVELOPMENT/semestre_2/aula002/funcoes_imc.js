const prompt = require('prompt-sync')()
function getUserInfo(){
    let peso = parseFloat(prompt('Qual é o seu peso?'))
    let altura = parseFloat(prompt('Qual é a sua altura?'))
   
    return {
        pesoInformado:peso,
        alturaInformada:altura
    }
}


function imc(peso, altura){
    return altura / peso ** 2
}


function main() {
    let peso, = getUserInfo().pesoInformado
    let altura = getUserInfo().alturaInformada
    let resultadoImc = imc(peso, altura)

    console.log(`O seu imc é ${resultadoImc}`)
}


const imprimir = (text) => {console.log(text)}

main()