function abrirMenu() {
    // Mostrar el menú
    document.getElementById("menu-lateral").classList.add("abierto");
    // Ocultar el botón de apertura
    document.getElementById("btn-menu").classList.add("oculto");
}

function cerrarMenu() {
    // Ocultar el menú
    document.getElementById("menu-lateral").classList.remove("abierto");
    // Mostrar el botón de apertura
    document.getElementById("btn-menu").classList.remove("oculto");
}