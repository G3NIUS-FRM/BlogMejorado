const DescriptionButton=document.getElementById("crear_description");
const modalDescription=document.getElementById("description_modal");
const formDescription=document.getElementById("description_form");
const cerrarModal=document.getElementById("cerrar_modal_description");
const modalOverlay=document.getElementById("modal_overlay");
DescriptionButton.addEventListener("click", () => {
    modalDescription.style.display = "block";
    modalOverlay.style.display="block";
});

cerrarModal.addEventListener("click", ()=>{
    modalDescription.style.display= "none";
    modalOverlay.style.display="none";
});

formDescription.addEventListener("submit", ()=>{
    modalDescription.style.display="none";
    modalOverlay.style.display="none";
});

const botonInformacion =document.getElementById("buttonInfo")
const cerrarModalInformacion=document.getElementById("cerrar_modal_informacion")
const InformacionForm=document.getElementById("Informacion-form")
const modalInformacion=document.getElementById("Informacion-modal")
botonInformacion.addEventListener('click', ()=>{
    modalOverlay.style.display="block";
    modalInformacion.style.display="block";
})
cerrarModalInformacion.addEventListener("click", ()=>{
    modalOverlay.style.display="none";
    modalInformacion.style.display="none";
})

InformacionForm.addEventListener("submit", ()=>{
    modalOverlay.style.display="none";
    modalInformacion.style.display="none";
})


