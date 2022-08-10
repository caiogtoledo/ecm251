public class Jogada {
    private EnumJogadas venco1;
    private EnumJogadas venco2;

    public Jogada(EnumJogadas venco1, EnumJogadas venco2) {
        this.venco1 = venco1;
        this.venco2 = venco2;
    }

    public boolean verificarVenceu(Jogada jogada){
        if(jogada.getTipo().equals(venco1) || jogada.getTipo().equals(venco2))
            return true;
        return false;
    }

    public EnumJogadas getTipo(){
        return EnumJogadas.LAGARTO;
    }
}