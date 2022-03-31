public class Sistema {
    public void run(){
        System.out.println("Estado inicial:");
        Usuarios todoUsuarios = new Usuarios();
        Usuario usuario1 = new Usuario(
            "Caio", 
            "senha123", 
            "caio@caio.com"
            );
        Conta conta1 = new Conta(usuario1, "1");
        todoUsuarios.setNovoUsuario(usuario1);
        conta1.depositar(1000);
        System.out.println(conta1.visualizarConta());

        Usuario usuario2 = new Usuario(
            "Bruno", 
            "senha123", 
            "bruno@bruno.com"
            );
        Conta conta2 = new Conta(usuario2, "2");
        todoUsuarios.setNovoUsuario(usuario2);
        conta2.depositar(300);
        System.out.println(conta2.visualizarConta()); 

        Transacao transacao1 = new Transacao();
        String QrCodeTransacao1 = transacao1.gerarQrCode(conta1, 100);
        System.out.println(QrCodeTransacao1);



        System.out.println("Estado final:");
        System.out.println(conta1.visualizarConta()); 
        System.out.println(conta2.visualizarConta()); 

    }
}
