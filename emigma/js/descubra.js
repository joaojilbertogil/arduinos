// Descubra o número
let numero = parseInt(prompt('Digite um número: '));

document.write('Você informou o número '+numero+ '<br>');

if (numero >=100){
    document.write('Número menor que 100'+ '<br/>');
    document.write('<img src="images/palhaco.png" alt="Sumio"');
}
else if (numero >=50){
    document.write('Número maior que 50'+ '<br>')
    document.write('<img src="images/bingo.jpg" alt="Não eta aqui">');
}

else if (numero >=25){
    document.write('Número maior que 25'+ '<br>')
    document.write('<img src="images/bozo.jpg" alt="Não eta aqui">');
}


else{
    document.write('Número menor que 100'+ '<br>')
    document.write('<img src="images/bozo.jpg" alt="Não eta aqui">');
}