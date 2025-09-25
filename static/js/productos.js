

document.querySelector("#main-form").addEventListener("submit", () => {
    
fetch("api/productos", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    nombre: document.querySelector("#nombre").value,
    categoria: document.querySelector("#categoria").value,
    precio: document.querySelector("#precio").value,
    stock: document.querySelector("#stock").value,
    stock_minimo: document.querySelector("#stock_minimo").value
  }),
}).then(respuesta => respuesta.json())
  .then(datos => console.log(datos))
});



fetch("/api/productos/")
.then(response => response.json())
.then(datos => {
    console.log(datos[0].categoria)
    const lista = document.querySelector("#listaproductos");
    for (dato of datos) {
        element = document.createElement("li")
        element.textContent = dato.nombre
        lista.appendChild(element)
    }
});