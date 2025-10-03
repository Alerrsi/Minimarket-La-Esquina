import {create} from "./create.js";
import {update, poblar} from "./update.js";


const form = document.querySelector("#main-form");
const nombre = document.querySelector("#nombre");
const categoria = document.querySelector("#categoria");
const precio = document.querySelector("#precio");
const stock = document.querySelector("#stock");
const stock_minimo = document.querySelector("#stock_minimo");



if (form.dataset.ruta == "update") {
  poblar(form.dataset.idproduct)
} 



// envio de formulario
document.querySelector("#main-form").addEventListener("submit", (e) => {
  e.preventDefault(); 
    // errores de mensajes
    const mensaje_stock = document.querySelector("#mensaje_stock");
    mensaje_stock.textContent = "";
    const mensaje_precio = document.querySelector("#mensaje_precio");
    mensaje_precio.style.display = "None"


  if (precio.value < 0) {
    mensaje_precio.classList.add("mensaje-error");
    mensaje_precio.textContent = "*El precio debe ser positivo";
    console.log("El precio debe ser positivo");
     e.preventDefault(); 
  }

  if (Number(stock.value) < Number(stock_minimo.value)) {
    console.log("valor stock" + stock.value)
    console.log("valor stock minimo" + stock_minimo.value)
    
    mensaje_stock.classList.add("mensaje-error");
    mensaje_stock.textContent = "*El stock debe ser mayor al stock minimo";
    console.log("El stock debe ser mayor al stock minimo");
    e.preventDefault()
  }

  
// codigo para crear  un producto
 if (form.dataset.ruta == "create") {
    create(nombre, categoria, precio, stock, stock_minimo)
  } else {
    update(form, nombre, categoria, precio, stock, stock_minimo)
  }

});