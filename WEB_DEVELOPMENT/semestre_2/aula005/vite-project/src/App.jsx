import './App.css'
import { useState , useEffect} from 'react';

function App() {

  const [contador, setContador] = useState(0)
  const [photos, setPhotos] = useState([])


  function aumentar(){
    setContador(contador + 1)

  }

  function zerar(){
    setContador(0)
  }

  function diminuir(){
    setContador(contador - 1)
  }

  useEffect(() => { // para auximliar a pagina a pegar infos externas

    fetch('https://jsonplaceholder.typicode.com/photos') // puxa a API
    .then(response => response.json())
    .then(data => setPhotos(data)) //async

  },[])
  

  return (
    <>
    <h1>Contador</h1>
    <p>{contador}</p>
    <button onClick={aumentar}>Aumentar</button>
    <button onClick={diminuir}>Diminuir</button>
    <button onClick={zerar}>Zerar</button>


    <h1>Fotos</h1>
    {photos.map((item) => (

      <img key= {item.id} src={item.url} alt= {item.title} width={50}/>

    ))}

    </>
  )
}

export default App
