public class App {
    public static void main(String[] args) throws Exception {
        Produto cornDog = new Comida(
                12.5,
                "CornDog",
                1,
                "Cachorro quente esquisito",
                EnumCategoriaComida.COREANA,
                EnumAlergicos.GLUTEM,
                EnumPimenta.COREANO);

        Produto acaiMoleza = new Bebida(
                15.5,
                "Açai do moleza",
                1, "Açai brabo",
                EnumCategoriaBebida.SUCO,
                EnumTemperatura.FRIO
            );

        System.out.println("Preços regulares:");
        System.out.println(cornDog.getNome()+" R$"+cornDog.getPreco());
        System.out.println(acaiMoleza.getNome()+" R$"+acaiMoleza.getPreco());

        System.out.println("Preços com desconto:");

        System.out.println("Preços Com Desconto:");
        System.out.println(cornDog.getNome()+":R$"+precoComDesconto(cornDog));
        System.out.println(acaiMoleza.getNome()+":R$"+precoComDesconto(acaiMoleza));
    }

    public static String precoComDesconto(IGerarDesconto produto){
        return "R$"+produto.gerarDesconto();
    }
}

