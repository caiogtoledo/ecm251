public class Conta {
    private String idConta;
    private double saldo;
    private Usuario usuario;

    public Conta(Usuario usuario, String idConta){
        this.idConta = idConta;
        this.usuario = usuario;
        saldo = 0;
    }   

    public String visualizarSaldo(){
        return  String.format("R$ %.2f", saldo);
    }

    public String visualizarConta(){
        return  String.format("Nome: %s - Saldo: R$ %.2f", usuario.getNome(), saldo);
    }

    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }

    public String getIdConta(){
        return idConta;
    }

    public Usuario getUsuario(){
        return usuario;
    }
}