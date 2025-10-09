
const proveedorSelect = document.querySelector("#proveedor");
const productoSelect = document.querySelector("#producto");


const poblarSelect = (element, entidad) => {
    fetch(`/api/${entidad}`).
    then(response => response.json()).
    then(datos => {
        for (dato of datos) {
            element.innerHTML += `
                <option value="${dato.id}">${dato.nombre}</option>
            `
        }
    })
} 


poblarSelect(proveedorSelect, "proveedores")
poblarSelect(productoSelect, "productos")