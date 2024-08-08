const button = document.querySelector('button');
const poupup = document.querySelector('.poupup-weapper');

const openClick = function(){poupup.classList.add("d-block");};

const openEventModal = function(event){
    clickOfElement = event.target.classList[0];
    const classListNameArray  = ['poupup-weapper','poupop-link','poupop-close']; //Se o usuario clicar em qualquer uma dessas classes o modal fecha
    const isClassList = classListNameArray.includes(clickOfElement) // se a lista inclui e evento que foi clicado

    if (isClassList){
        poupup.classList.remove("d-block"); //remove o block volta a ser none
    }
}

button.addEventListener("click",openClick);
poupup.addEventListener("click",openEventModal);

