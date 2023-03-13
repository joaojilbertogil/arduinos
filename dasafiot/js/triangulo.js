//Triângulo
let sideA = parseInt(prompt('Digite o lada A: '));
let sideB = parseInt(prompt('Digite o lada B: '));
let sideC = parseInt(prompt('Digite o lada C: '));

//Testar a Validade
if(sideA <= sideB + sideC &&
   sideB <= sideA + sideC &&
   sideC <= sideA + sideB ){
    
    if (sideA == sideB && sideA == sideC){
    document.write('Esse Triângulo é Equilatero'+ '<br>')
        document.write('<img src="images/figura1.jpg" alt="Não eta aqui">');
    }

     else if(sideA == sideB || sideA == sideC) {
        document.write('Esse Triângulo é Isosceles'+ '<br>')
        document.write('<img src="images/figura2.jpg" alt="Não eta aqui">');
     }

        else{
            document.write('Esse Triângulo é Escaleno'+ '<br>')
        document.write('<img src="images/figura3.png" alt="Não eta aqui">');

        } 

     }  

   

   
    else{
        document.write('Não é Triângulo'+ '<br>')
        document.write('<img src="images/erro.jpg" alt="Não eta aqui">');
    }
   