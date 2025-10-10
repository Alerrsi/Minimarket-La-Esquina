const eliminar = (id) => {
  fetch("/api/compras/" + id + "/", { method: "DELETE" })
    .then(response => {
      location.reload();
    });
};

const proveedorNombre = async (id) => {
  try {
    const response = await fetch(`/api/proveedores/${id}`);
    if (!response.ok) throw new Error("Error al obtener la categoría");
    const data = await response.json();
    return data.nombre;
  } catch (error) {
    console.error(error);
    return "Desconocida";
  }
};

const cargarProductos = async () => {
  const table = document.querySelector("#main-table");
  const response = await fetch("/api/proveedores/");
  const datos = await response.json();

  for (const dato of datos) {
    const nombreProveedor = await proveedorNombre(dato.categoria);

    table.innerHTML += `
      <tr class="hover:bg-gray-50">
        <td class="px-6 py-4 whitespace-nowrap">
          <div class="flex items-center">
            <div class="ml-4">
              <div class="text-sm font-medium text-gray-900">${dato.id}</div>
            </div>
          </div>
        </td>
        <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${nombreProveedor}</td>
        <td class="px-6 py-4 whitespace-nowrap">${dato.total}</td>
        <td class="px-6 py-4 whitespace-nowrap">${dato.productos}</td>
        </td>
      </tr>
    `;
  }
};

// Ejecutar cuando cargue la página
cargarProductos();
