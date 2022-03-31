public class Usuario {
    private String nome;
    private String senha;
    private String email;

    public Usuario(String nome, String senha, String email){
        this.nome = nome;
        this.email = email;
        this.setSenha(senha);
    }


    public void visualizarCliente(){
        System.out.println("Dados do Usuário:");
        System.out.println("Nome:" + nome);
        System.out.println("E-mail:" + email);
        
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getNome(){
        return nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getEmail(){
        return email;
    }
   
    public void setEmail(String email){
        this.email = email;
    }
}
