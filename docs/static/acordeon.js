function toggleAccordion(element) {
    const content = element.nextElementSibling;

    // Cerrar todos los demás elementos abiertos
    const allContents = document.querySelectorAll('.accordion-content');
    allContents.forEach((item) => {
        if (item !== content) {
            item.style.maxHeight = null;
        }
    });

    // Alternar el estado del contenido actual
    if (content.style.maxHeight) {
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
    }
}