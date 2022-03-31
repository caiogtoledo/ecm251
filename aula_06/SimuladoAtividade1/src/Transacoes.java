import java.util.ArrayList;

public class Transacoes {
    private ArrayList<Transacao> todasTransacoes;
    
    public void registraTransacao(Transacao transacao){
        todasTransacoes.add(transacao);
    }

    public ArrayList<Transacao> getTodasTransacoes(){
        return todasTransacoes;
    }

}
