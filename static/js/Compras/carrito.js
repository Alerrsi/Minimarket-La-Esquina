const form = document.querySelector("#main-form");
const producto_id = document.querySelector("#producto");
const cantidad = document.querySelector("#cantidad");
const table = document.querySelector("#tabla");

const productos = [];
const agregarProducto = (lista, producto, cantidadInput, tabla) => {
    // Creamos el objeto del nuevo producto
    const nuevoProducto = {
        "producto": producto,
        "cantidad": cantidadInput
    };

    // Lo agregamos al array
    lista.push(nuevoProducto);

    // Creamos la fila solo para este nuevo producto
    const row = document.createElement("tr");
    row.className = "hover:bg-gray-50 transition-colors";

    row.innerHTML = `
        <td class="px-4 py-4 text-sm text-gray-900">${nuevoProducto.producto.options[nuevoProducto.producto.selectedIndex].text}</td>
        <td class="px-4 py-4 text-sm text-gray-900 text-center">${nuevoProducto.cantidad}</td>
        <td class="px-4 py-4 text-sm text-gray-900 text-right font-medium"></td>
        <td class="px-4 py-4 text-center">
            <div class="flex items-center justify-center gap-2">
                <button id = "editar" class="text-blue-600 hover:text-blue-800 transition-colors" title="Editar">Editar</button>
                <button id = "eliminar"  class="text-red-600 hover:text-red-800 transition-colors" title="Eliminar">Eliminar</button>
            </div>
        </td>
    `;

    tabla.appendChild(row);

};


const eliminarProducto = (lista, elemento) => {
    lista = lista.filter(e => e != elemento)
}
 
if (productos.length > 0) {
    const eliminar = document.querySelector("#eliminar")

    eliminar.addEventListener("click", () => {
        eliminarProducto(productos, {
            "producto":producto_id,
            "cantidad": cantidad.value 
        })
    })


};    






form.addEventListener("submit", (e) => {
    console.log("submittt");
    e.preventDefault();
    agregarProducto(productos, producto_id, cantidad.value, table);

});






