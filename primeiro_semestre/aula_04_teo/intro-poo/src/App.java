
public class App {
    public static void main(String[] args) {
        //Declarando e Instancia um objeto Caneta
        Caneta c1 = new Caneta();
        c1.modelo = "BIC";
        c1.cor = "Azul";
        c1.carga = 100;
        c1.ponta = 1.0;

        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Vermelha", "Stabillo", 0.4);

        System.out.println("Minha Caneta: " + c1.mostrarDados());
       
        System.out.println("Minha Caneta: " + c2.mostrarDados());

        c1.escrever("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb aaa");
        c1.escrever("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb aaa");
        System.out.println("Minha Caneta: " + c1.mostrarDados());
       
        System.out.println("Minha Caneta: " + c2.mostrarDados());
    }
}
