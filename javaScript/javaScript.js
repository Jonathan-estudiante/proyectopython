var total=0;
var sumaFilas=document.querySelectorAll(".row_costo");

filas.forEach(function(e) {
 
    // obtenemos las columnas de cada fila
    var columnas=e.querySelectorAll("td");

    // obtenemos los valores de la cantidad y importe
    var suma=parseFloat(columnas[3].textContent);

    // mostramos el total por fila
    columnas[3].textContent=(suma);

    total+=suma;
});

var filas=document.querySelectorAll(".totalcursojs");
