document.addEventListener('DOMContentLoaded', mostrarRecetas);
document.getElementById('form-receta').addEventListener('submit', guardarReceta);

function guardarReceta(e) {
  e.preventDefault();

  const titulo = document.getElementById('titulo').value.trim();
  const ingredientes = document.getElementById('ingredientes').value.trim();
  const instrucciones = document.getElementById('instrucciones').value.trim();

  if (!titulo || !ingredientes || !instrucciones) return;

  const receta = { titulo, ingredientes, instrucciones };

  let recetas = JSON.parse(localStorage.getItem('recetas')) || [];
  recetas.push(receta);
  localStorage.setItem('recetas', JSON.stringify(recetas));

  document.getElementById('form-receta').reset();
  mostrarRecetas();
}

function mostrarRecetas() {
  const lista = document.getElementById('lista-recetas');
  lista.innerHTML = '';

  const recetas = JSON.parse(localStorage.getItem('recetas')) || [];

  recetas.forEach((receta, index) => {
    const div = document.createElement('div');
    div.className = 'receta';
    div.innerHTML = `
      <h3>${receta.titulo}</h3>
      <p><strong>Ingredientes:</strong><br>${receta.ingredientes.replace(/\n/g, '<br>')}</p>
      <p><strong>Instrucciones:</strong><br>${receta.instrucciones}</p>
      <button onclick="eliminarReceta(${index})">Eliminar</button>
    `;
    lista.appendChild(div);
  });
}

function eliminarReceta(index) {
  let recetas = JSON.parse(localStorage.getItem('recetas')) || [];
  recetas.splice(index, 1);
  localStorage.setItem('recetas', JSON.stringify(recetas));
  mostrarRecetas();
}
