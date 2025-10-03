
eliminar = (id) => {
    fetch("/api/productos/" + id + "/", {method : "DELETE"}).
        then(response => {
            location.reload()
        })            
}
    
const table = document.querySelector("#main-table");
fetch("/api/productos/").
then(response => response.json()).
then(datos => {
    for (dato of datos) {


        table.innerHTML += `
            <tr class="hover:bg-gray-50">
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <div class="flex items-center">
                                        <div class="ml-4">
                                            <div class="text-sm font-medium text-gray-900">${dato.id}</div>
                                        </div>
                                    </div>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${dato.nombre}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">${dato.categoria}</td>
                                <td class="px-6 py-4 whitespace-nowrap">${dato.precio}</td>
                                <td class="px-6 py-4 whitespace-nowrap">${dato.stock}</td>
                                <td class="px-6 py-4 whitespace-nowrap">${dato.stock_minimo}</td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                                    
                                        <button onclick = actualizar(${dato.id}) class="text-primary hover:text-green-800 mr-3">Editar</button>
                                    

                                    
                                        <button onclick= "eliminar(${dato.id})" class="text-red-600 hover:text-red-800">Eliminar</button>
                                    
                                </td>
                            </tr>
            ` 
            
            }})
          