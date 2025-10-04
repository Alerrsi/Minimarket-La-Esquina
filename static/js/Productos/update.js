export const update = (form, nombre, categoria, precio, stock, stock_minimo) => {
    fetch("/api/productos/" + form.dataset.idproduct + "/", {    
    method: "PUT",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(
        {
      nombre: nombre.value,
      categoria: categoria.value,
      precio: precio.value,
      stock: stock.value,
      stock_minimo: stock_minimo.value
    }
),
  })
  .then(async r => {

    const mensaje = document.querySelector("#mensaje");

    if (r.status == 200) {
      mensaje.style.color = "green";
      mensaje.textContent = "Producto Actualizado";
       window.location.href = "/Productos" 

    }else{
    mensaje.style.color = "red";
    const data = await r.json()

    if (data.nombre) {
      mensaje.textContent += data.nombre;
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

    if (data.non_field_errors) {
         mensaje.textContent = data.non_field_errors;
    }

    
    }

  })
  .catch(err => console.log())
}


export const poblar = (id, nombre, categoria, precio, stock, stock_minimo) => {
  fetch(`/api/productos/${id}`).
  then(response => response.json()).
  then( data =>{
    nombre.value = data["nombre"]
    categoria.value = data["categoria"]
    precio.value = data["precio"]
    stock.value = data["stock"]
    stock_minimo.value = data["stock_minimo"]
  }
  )
}
