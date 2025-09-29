document.querySelector("#main-form").addEventListener("submit", (e) => {
  e.preventDefault(); 
  const nombre = document.querySelector("#nombre").value;
  const categoria = document.querySelector("#categoria").value;
  const precio = document.querySelector("#precio").value;
  const stock = document.querySelector("#stock").value;
  const stock_inicial = document.querySelector("#stock_minimo").value;

  if (precio < 0) {
    const mensaje = document.querySelector("#mensaje_precio");
    mensaje.classList.add("mensaje-error");
    mensaje.textContent = "*El precio debe ser positivo";
    console.log("El precio debe ser positivo");
     e.preventDefault(); 
  }

  if (stock < stock_inicial) {
    const mensaje = document.querySelector("#mensaje_stock");
    mensaje.classList.add("mensaje-error");
    mensaje.textContent = "*El stock debe ser mayor al stock minimo";
    console.log("El stock debe ser mayor al stock minimo");
    e.preventDefault()
  }



  

 fetch("/api/productos/", {    
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(
        {
      nombre: document.querySelector("#nombre").value,
      categoria: document.querySelector("#categoria").value,
      precio: document.querySelector("#precio").value,
      stock: document.querySelector("#stock").value,
      stock_minimo: document.querySelector("#stock_minimo").value
    }
),
  })
  .then(async r => {

    const mensaje = document.querySelector("#mensaje");

    if (r.status == 201) {
      mensaje.style.color = "green";
      mensaje.textContent = "Producto Guardado";

    }else{
    mensaje.style.color = "red";
    const data = await r.json()

    if (data.nombre) {
      mensaje.textContent = data.nombre;
    }

    if (data.categoria) {
      mensaje.textContent = data.categoria;
    }

    if (data.precio) {
      mensaje.textContent = data.precio;
    }

    if (data.stock) {
      mensaje.textContent = data.stock;
    }

    if (data.stock_minimo) {
      mensaje.textContent = data.stock_minimo;
    }
    }

  })
  .catch(err => console.log())});

