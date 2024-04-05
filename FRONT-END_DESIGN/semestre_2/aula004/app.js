//cookies
document.cookie = "username=Caio; expires=Thu, 14 Dec 2023 12:00:00 UTC; path=/" 
                                  //Quando expira                       // quais paginas armazenam o cookie

//Local Storage (fica guardado no seu computador) (so armazena string)
localStorage.setItem('nome', "Rafael")
nomeLocalStorage = localStorage.getItem('nome')
console.log(nomeLocalStorage)
localStorage.removeItem('nome') //remove um item
localStorage.clear() //limpa tudo

//Sesion Storage (somente durante as sessões)
sessionStorage.setItem('idade',10)


//JSON
let nomes = ['caio', 'carol', 'lucas']
const nomeJson = JSON.stringify(nomes)
JSON.parse(localStorage.getItem('nome', 'Rafa'))