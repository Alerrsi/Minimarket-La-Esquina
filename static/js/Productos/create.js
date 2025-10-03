export const create = (nombre, categoria, precio, stock, stock_minimo) => {
    console.log("POST")
    fetch("/api/productos/", {    
    method: "POST",
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

    if (r.status == 201) {
        mensaje.style.color = "green";
        mensaje.textContent = "Producto Guardado";
        form.reset();
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