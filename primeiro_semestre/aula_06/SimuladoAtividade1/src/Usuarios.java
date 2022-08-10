import java.util.ArrayList;

public class Usuarios {
    private ArrayList<Usuario> listaDeUsuarios;

    public Usuarios(){
        this.listaDeUsuarios = new ArrayList<>();
    }

    public void visualizarListaDeUsuarios(){
        System.out.println("Todos Usuários:");
        //fazer o for para printar a lista
    }

    public ArrayList<Usuario> getListaDeUsuarios(){
        return listaDeUsuarios;
    }

    public void setNovoUsuario(Usuario usuario){
        this.listaDeUsuarios.add(usuario);
    }
}
