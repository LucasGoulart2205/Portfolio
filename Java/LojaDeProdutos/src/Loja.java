public class Loja {
    private Produto produto1;
    private Produto produto2;
    private Produto produto3;

    public void adicionarProduto(Produto produto) {
        if (this.produto1 == null) {
            this.produto1 = produto;
        } else if (this.produto2 == null) {
            this.produto2 = produto;
        } else if (this.produto3 == null) {
            this.produto3 = produto;
        } else {
            System.out.println("Todos os produtos foram preenchidos");
        }
    }

    public void removerProduto(Produto produto) {
        if (this.produto1 == produto) {
            this.produto1 = null;
        } else if (this.produto2 == produto) {
            this.produto2 = null;
        } else if (this.produto3 == produto) {
            this.produto3 = null;
        } else {
            System.out.println("Nao encontrado");
        }
    }

    public void listarProdutos() {
        if (this.produto1 != null) {
            imprimirProduto(this.produto1);
        }
        if (this.produto2 != null) {
            imprimirProduto(this.produto2);
        }
        if (this.produto3 != null) {
            imprimirProduto(this.produto3);
        }

    }

    private void imprimirProduto(Produto produto) {
        System.out.println("\n•Nome do produto: " + produto.getNome() + "\nPreço: " + produto.getPreco() + "\nQuantidade: " + produto.getQuantidade());
    }

    public void venderProduto(Produto produto, int quantidade) {
        if (this.produto1 == produto) {
            if (this.produto1.getQuantidade() >= quantidade) {
                int quantidadeProduto = this.produto1.getQuantidade();
                quantidadeProduto = quantidadeProduto - quantidade;
                this.produto1.setQuantidade(quantidadeProduto);
            } else if (this.produto2 == produto) {
                if (this.produto2.getQuantidade() >= quantidade) {
                    int quantidadeProduto = this.produto2.getQuantidade();
                    quantidadeProduto = quantidadeProduto - quantidade;
                    this.produto2.setQuantidade(quantidadeProduto);
                }
            } else if (this.produto3 == produto) {
                if (this.produto3.getQuantidade() >= quantidade) {
                    int quantidadeProduto = this.produto3.getQuantidade();
                    quantidadeProduto = quantidadeProduto - quantidade;
                    this.produto3.setQuantidade(quantidadeProduto);

                }
            } else {
                System.out.println("Produto nao encontrado");
            }
        }
    }

    public void adcionarEstoque(Produto produto, int quantidade) {
        if (this.produto1 == produto) {
            this.produto1.setQuantidade(this.produto1.getQuantidade() + quantidade);
        } else if (this.produto2 == produto) {
            this.produto2.setQuantidade((this.produto2.getQuantidade() + quantidade));
        } else if (this.produto3 == produto) {
            this.produto3.setQuantidade((this.produto2.getQuantidade() + quantidade));
        }

    }
}