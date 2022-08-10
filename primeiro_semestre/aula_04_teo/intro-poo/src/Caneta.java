public class Caneta{
    // Atributos
    String modelo;
    String cor;
    double ponta;
    int carga;
    final int CARGA_INICIAL = 100;

    void iniciarCaneta(String cor, String modelo, double ponta){
        this.cor = cor;
        this.modelo = modelo;
        this.ponta = ponta;
        this.carga = CARGA_INICIAL;
    }

    //Métodos
    void escrever(String texto){
        
        if( texto.length() > this.carga){
            String textCanPrint = "";
            for(int i = 0;  i <= this.carga;  i++){
                textCanPrint += texto.split("")[i];
            }
            System.out.println(textCanPrint);
            System.out.println("Caneta sem carga!");
            this.carga -= texto.length();
            
        }else{
            System.out.println(texto);
            this.carga -= texto.length();
        }
        
    }

    String mostrarDados(){
        return "Modelo:" 
        + this.modelo 
        + " - Cor:" 
        + this.cor 
        + " - Carga:" 
        + this.carga 
        +  " - Ponta:" 
        + this.ponta;
    }
}