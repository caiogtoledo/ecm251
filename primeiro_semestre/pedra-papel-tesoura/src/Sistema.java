import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static void run() {
        // Usuario escolhe a jogada
        Jogada jogada1 = new Pedra();
        // Sorteio da jogada para o PC
        Jogada jogada2 = sortearJogada();
        // Avaliação das jogadas
        String resultado = avaliaJogadas(jogada1, jogada2);
        // Exibição do resultado
        System.out.println("Resultado:" + resultado);
    }

    private static Jogada sortearJogada() {
        Jogada jogadas[] = new Jogada[5];
        jogadas[0] = new Pedra();
        jogadas[1] = new Papel();
        jogadas[2] = new Tesoura();
        jogadas[3] = new Lagarto();
        jogadas[4] = new Spock();

        return jogadas[ThreadLocalRandom.current().nextInt(jogadas.length)];
    }

    private static String avaliaJogadas(Jogada jogada1, Jogada jogada2) {
        if (jogada1.verificarVenceu(jogada2))
            return "Jogada 1 " + jogada1.getTipo() + " Ganhou de " + jogada2.getTipo();
        if (jogada2.verificarVenceu(jogada1))
        return "Jogada 2 " + jogada2.getTipo() + "Ganhou de " + jogada1.getTipo();
        return "Empate";
    }
}