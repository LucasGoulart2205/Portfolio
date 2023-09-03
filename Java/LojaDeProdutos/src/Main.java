public class Main {
    public static void main(String[] args) {
        Produto camisa = new Produto();
        camisa.setNome("Gola polo");
        camisa.setPreco(99.99);
        camisa.setQuantidade(200);

        Produto calca = new Produto();
        calca.setNome("Jeans");
        calca.setPreco(300);
        calca.setQuantidade(100);

        Produto tenis = new Produto();
        tenis.setNome("Jordan");
        tenis.setPreco(180);
        tenis.setQuantidade(100);

        Loja loja1 = new Loja();
        loja1.adicionarProduto(camisa);
        loja1.adicionarProduto(calca);
        loja1.adicionarProduto(tenis);

        System.out.println("\n•Estoque 1: ");
        loja1.listarProdutos();
        loja1.removerProduto(calca);
        System.out.println("\n•Estoque 2:  ");
        loja1.listarProdutos();
    }
}
