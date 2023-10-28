function teste(arg1, arg2){
    console.log(arg1 + arg2)


}

function impimeNome(name){
    console.log(`Meu Nome é ${name}`)

}

impimeNome('Rafael')
teste(10,10);

function cliqueAqui(){
    alert('olá')
}


const tirarDiv = document.querySelector('.tirarDiv');
const VoltarDiv = document.querySelector('.voltarDiv');
const card = document.querySelector('.card')

tirarDiv.addEventListener('click', function(){
    card.style.display = 'none';
});

VoltarDiv.addEventListener('click', function(){
    card.style.display = 'flex'
});


