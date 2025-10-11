const form = document.querySelector("#main-form");
const producto_id = document.querySelector("#producto");
const cantidad = document.querySelector("#cantidad");
const costo_unitario = document.querySelector("#costo_unitario");
const proveedor = document.querySelector("#proveedor");
const table = document.querySelector("#tabla");
const enviarCompraBtn = document.querySelector("#enviar-compra");
const limpiarCarritoBtn = document.querySelector("#limpiar-carrito");
const confirmarCompraBtn = document.querySelector("#confirmar-compra");
const cancelarCompraBtn = document.querySelector("#cancelar-compra");
const cerrarResultadoBtn = document.querySelector("#cerrar-resultado");

// REMOVER estas líneas - ya están en el HTML
// const confirmModal = document.getElementById('confirmModal');
// const resultModal = document.getElementById('resultModal');

const productos = [];

// Función para formatear moneda
const formatearMoneda = (valor) => {
    return new Intl.NumberFormat('es-CL', {
        style: 'currency',
        currency: 'CLP'
    }).format(valor);
};

// Función para actualizar totales
const actualizarTotales = () => {
    const totalCarrito = productos.reduce((total, producto) => {
        return total + (producto.cantidad * producto.costo_unitario);
    }, 0);

    const totalCarritoElement = document.querySelector("#total-carrito");
    const totalGeneralElement = document.querySelector("#total-general");
    
    if (totalCarritoElement) {
        totalCarritoElement.textContent = formatearMoneda(totalCarrito);
    }
    if (totalGeneralElement) {
        totalGeneralElement.textContent = formatearMoneda(totalCarrito);
    }
};

// Función para crear una fila de producto
const crearFilaProducto = (producto, index, tabla) => {
    const row = document.createElement("tr");
    row.className = "hover:bg-gray-50 transition-colors producto-item";
    row.dataset.index = index;

    const subtotal = producto.cantidad * producto.costo_unitario;

    row.innerHTML = `
        <td class="px-4 py-4 text-sm text-gray-900">${producto.nombre}</td>
        <td class="px-4 py-4 text-sm text-gray-900 text-center">${producto.cantidad}</td>
        <td class="px-4 py-4 text-sm text-gray-900 text-right">${formatearMoneda(producto.costo_unitario)}</td>
        <td class="px-4 py-4 text-sm text-gray-900 text-right font-medium">${formatearMoneda(subtotal)}</td>
        <td class="px-4 py-4 text-center">
            <div class="flex items-center justify-center gap-2">
                <button class="btn-editar" title="Editar" data-index="${index}">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
                    </svg>
                </button>
                <button class="btn-eliminar" title="Eliminar" data-index="${index}">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                    </svg>
                </button>
            </div>
        </td>
    `;

    tabla.appendChild(row);

    // Agregar event listeners a los botones
    const btnEliminar = row.querySelector('.btn-eliminar');
    const btnEditar = row.querySelector('.btn-editar');

    btnEliminar.addEventListener('click', () => eliminarProducto(index));
    btnEditar.addEventListener('click', () => editarProducto(index));
};

// Función para agregar producto al carrito
const agregarProducto = (lista, producto, cantidadInput, costoUnitario, tabla) => {
    // Validar que todos los campos estén completos
    if (!producto?.value || !cantidadInput || !costoUnitario) {
        mostrarResultado('Error', 'Por favor, complete todos los campos del producto.', 'error');
        return;
    }

    // Crear el objeto del nuevo producto
    const nuevoProducto = {
        "producto": parseInt(producto.value),
        "cantidad": parseInt(cantidadInput),
        "costo_unitario": parseFloat(costoUnitario),
        "nombre": producto.options[producto.selectedIndex]?.text || `Producto ${producto.value}`
    };

    // Verificar si el producto ya existe en el carrito
    const productoExistente = lista.findIndex(p => p.producto === nuevoProducto.producto);
    if (productoExistente !== -1) {
        // Actualizar cantidad si el producto ya existe
        lista[productoExistente].cantidad += nuevoProducto.cantidad;
        // Actualizar la fila existente
        actualizarFilaProducto(lista[productoExistente]);
    } else {
        // Agregar nuevo producto
        lista.push(nuevoProducto);
        // Crear nueva fila
        crearFilaProducto(nuevoProducto, lista.length - 1, tabla);
    }

    // Actualizar totales
    actualizarTotales();

    // Limpiar formulario
    if (cantidad) cantidad.value = '';
    if (costo_unitario) costo_unitario.value = '';
    if (producto_id) producto_id.focus();
};

// Función para actualizar una fila existente
const actualizarFilaProducto = (producto) => {
    const rows = table.querySelectorAll('tr[data-index]');
    const productoIndex = productos.indexOf(producto);
    
    if (productoIndex === -1) return;
    
    const row = Array.from(rows).find(r => parseInt(r.dataset.index) === productoIndex);
    
    if (row) {
        const subtotal = producto.cantidad * producto.costo_unitario;
        row.innerHTML = `
            <td class="px-4 py-4 text-sm text-gray-900">${producto.nombre}</td>
            <td class="px-4 py-4 text-sm text-gray-900 text-center">${producto.cantidad}</td>
            <td class="px-4 py-4 text-sm text-gray-900 text-right">${formatearMoneda(producto.costo_unitario)}</td>
            <td class="px-4 py-4 text-sm text-gray-900 text-right font-medium">${formatearMoneda(subtotal)}</td>
            <td class="px-4 py-4 text-center">
                <div class="flex items-center justify-center gap-2">
                    <button class="btn-editar" title="Editar" data-index="${productoIndex}">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/>
                        </svg>
                    </button>
                    <button class="btn-eliminar" title="Eliminar" data-index="${productoIndex}">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/>
                        </svg>
                    </button>
                </div>
            </td>
        `;

        // Reagregar event listeners
        const btnEliminar = row.querySelector('.btn-eliminar');
        const btnEditar = row.querySelector('.btn-editar');

        btnEliminar.addEventListener('click', () => eliminarProducto(productoIndex));
        btnEditar.addEventListener('click', () => editarProducto(productoIndex));
    }
};

// Función para eliminar producto
const eliminarProducto = (index) => {
    if (index >= 0 && index < productos.length) {
        productos.splice(index, 1);
        renderizarCarrito();
        actualizarTotales();
    }
};

// Función para editar producto
const editarProducto = (index) => {
    const producto = productos[index];
    if (producto && producto_id && cantidad && costo_unitario) {
        producto_id.value = producto.producto;
        cantidad.value = producto.cantidad;
        costo_unitario.value = producto.costo_unitario;
        
        // Eliminar el producto para reemplazarlo
        eliminarProducto(index);
        producto_id.focus();
    }
};

// Función para renderizar todo el carrito
const renderizarCarrito = () => {
    if (!table) return;
    
    // Limpiar tabla
    table.innerHTML = '';
    
    // Renderizar cada producto
    productos.forEach((producto, index) => {
        crearFilaProducto(producto, index, table);
    });
};

// Función para limpiar carrito
const limpiarCarrito = () => {
    productos.length = 0;
    renderizarCarrito();
    actualizarTotales();
};

// Función para mostrar resultado
const mostrarResultado = (titulo, mensaje, tipo = 'success') => {
    const resultModal = document.getElementById('resultModal');
    if (!resultModal) return;
    
    const title = document.querySelector("#result-title");
    const message = document.querySelector("#result-message");
    
    if (!title || !message) return;
    
    title.textContent = titulo;
    message.textContent = mensaje;
    
    // Limpiar clases previas
    title.className = 'text-xl font-bold text-gray-900';
    message.className = 'text-gray-600 mb-6';
    
    if (tipo === 'error') {
        title.classList.add('text-red-600');
        message.classList.add('text-red-600');
    } else {
        title.classList.add('text-green-600');
        message.classList.add('text-green-600');
    }
    
    resultModal.classList.remove('hidden');
    resultModal.classList.add('flex');
};

// Función para enviar compra a la API
const enviarCompra = async () => {
    try {
        // Validar que haya productos y proveedor
        if (productos.length === 0) {
            mostrarResultado('Error', 'No hay productos en el carrito.', 'error');
            return;
        }

        if (!proveedor?.value) {
            mostrarResultado('Error', 'Debe seleccionar un proveedor.', 'error');
            return;
        }

        // Crear objeto de compra según la estructura requerida
        const compra = {
            "fecha": new Date().toISOString().split('T')[0], // Fecha actual en formato YYYY-MM-DD
            "proveedor": parseInt(proveedor.value),
            "productos": productos.map(p => ({
                "producto": p.producto,
                "cantidad": p.cantidad,
                "costo_unitario": p.costo_unitario
            }))
        };

        console.log('Enviando compra:', compra);

        // Obtener token CSRF
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

        if (!csrfToken) {
            throw new Error('No se pudo obtener el token CSRF');
        }

        // Enviar a la API
        const response = await fetch('/api/compras/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify(compra)
        });

        if (response.status == 201) {
            const result = await response.json();
            mostrarResultado('Éxito', 'Compra registrada correctamente.');
            limpiarCarrito();
        }else {
    const errorText = await response.text();
    let errorMessage = 'Error al enviar la compra.';

    try {
        const errorJson = JSON.parse(errorText);

        const mensajes = [];

        if (errorJson.fecha) {
            mensajes.push(`📅 Fecha: ${errorJson.fecha.join(', ')}`);
        }

        if (errorJson.proveedor) {
            mensajes.push(`🏢 Proveedor: ${errorJson.proveedor.join(', ')}`);
        }

        if (errorJson.productos && Array.isArray(errorJson.productos)) {
            errorJson.productos.forEach((prod, index) => {
                if (prod.producto) {
                    mensajes.push(`🧾 Producto ${index + 1}: ${prod.producto.join(', ')}`);
                }
                if (prod.cantidad) {
                    mensajes.push(`📦 Cantidad (producto ${index + 1}): ${prod.cantidad.join(', ')}`);
                }
                if (prod.non_field_errors) {
                    mensajes.push(`⚠️ Producto ${index + 1}: ${prod.non_field_errors.join(', ')}`);
                }
            });
        }

        if (mensajes.length > 0) {
            errorMessage = mensajes.join('\n');
        } else {
            // Si no coincide con los patrones esperados
            errorMessage = errorJson.detail || JSON.stringify(errorJson);
        }

    } catch (err) {
        // Si no se puede parsear el JSON
        errorMessage = errorText || 'Error inesperado al procesar la respuesta del servidor.';
    }

    throw new Error(errorMessage);
}


    } catch (error) {
        console.error('Error:', error);
        mostrarResultado('Error', `Error al enviar la compra: ${error.message}`, 'error');
    }
};

// Inicializar event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Event Listeners principales
    if (form) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            agregarProducto(productos, producto_id, cantidad.value, costo_unitario.value, table);
        });
    }

    if (enviarCompraBtn) {
        enviarCompraBtn.addEventListener("click", () => {
            if (productos.length === 0) {
                mostrarResultado('Error', 'No hay productos en el carrito.', 'error');
                return;
            }
            const confirmModal = document.getElementById('confirmModal');
            if (confirmModal) {
                confirmModal.classList.remove('hidden');
                confirmModal.classList.add('flex');
            }
        });
    }

    if (limpiarCarritoBtn) {
        limpiarCarritoBtn.addEventListener("click", limpiarCarrito);
    }

    if (confirmarCompraBtn) {
        confirmarCompraBtn.addEventListener("click", () => {
            const confirmModal = document.getElementById('confirmModal');
            if (confirmModal) {
                confirmModal.classList.add('hidden');
                confirmModal.classList.remove('flex');
            }
            enviarCompra();
        });
    }

    if (cancelarCompraBtn) {
        cancelarCompraBtn.addEventListener("click", () => {
            const confirmModal = document.getElementById('confirmModal');
            if (confirmModal) {
                confirmModal.classList.add('hidden');
                confirmModal.classList.remove('flex');
            }
        });
    }

    if (cerrarResultadoBtn) {
        cerrarResultadoBtn.addEventListener("click", () => {
            const resultModal = document.getElementById('resultModal');
            if (resultModal) {
                resultModal.classList.add('hidden');
                resultModal.classList.remove('flex');
            }
        });
    }

    // Inicializar totales
    actualizarTotales();
});