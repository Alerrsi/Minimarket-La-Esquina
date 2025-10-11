const eliminar = (id) => {
  fetch("/api/compras/" + id + "/", { method: "DELETE" })
    .then(response => location.reload());
};

// Obtener el nombre del proveedor por su ID
const proveedorNombre = async (id) => {
  try {
    const response = await fetch(`/api/proveedores/${id}`);
    if (!response.ok) throw new Error("Error al obtener el proveedor");
    const data = await response.json();
    return data.nombre || "Desconocido";
  } catch (error) {
    console.error(error);
    return "Desconocido";
  }
};

// Cargar compras desde /api/compras y poblar la tabla
const cargarCompras = async () => {
  const table = document.querySelector("#main-table tbody");
  table.innerHTML = ""; // limpiar tabla

  try {
    const response = await fetch("/api/compras/");
    if (!response.ok) throw new Error("Error al obtener compras");

    const compras = await response.json();

    for (const compra of compras) {
      const nombreProveedor = await proveedorNombre(compra.proveedor);

      // Generar listado de productos
      const productosHTML = compra.productos.length > 0
        ? `
          <ul class="list-disc pl-4">
            ${compra.productos
              .map(p => `<li>${p.nombre_producto} (x${p.cantidad}) - $${p.costo_unitario}</li>`)
              .join("")}
          </ul>
        `
        : "<em>Sin productos</em>";

      table.innerHTML += `
        <tr class="hover:bg-gray-50">
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${compra.fecha ?? "-"}</td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${nombreProveedor}</td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">$${compra.total ?? 0}</td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${productosHTML}</td>
          
        </tr>
      `;
    }

  } catch (error) {
    console.error("Error al cargar compras:", error);
    table.innerHTML = `<tr><td colspan="5" class="text-center text-red-500 py-4">Error al cargar compras</td></tr>`;
  }
};

// Ejecutar al cargar la página
cargarCompras();
