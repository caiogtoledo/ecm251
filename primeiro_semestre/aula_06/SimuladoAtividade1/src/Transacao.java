public class Transacao {
    public String gerarQrCode(Conta contaRecebedor, double valor){
        String idContaRecebedor = contaRecebedor.getIdConta();
        String nomeRecebedor = contaRecebedor.getUsuario().getNome();
        String dadosQrCode = idContaRecebedor + ";" + nomeRecebedor +";"+ valor;
        return dadosQrCode;
    }

    public void realizarPagamento(Conta contaPagador, String qrCode){
        String[] dadosQrCode = qrCode.split(";");
        contaPagador.sacar(Double.parseDouble(dadosQrCode[2]));
        // Buscar a conta na lista de todas as contas pelo id dadosQrCode[0])
        // depositar a quantia dadosQrCode[2]
    }
}
