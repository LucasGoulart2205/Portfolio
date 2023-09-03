public class Livro extends Produto {
    private String autor;
    private int anoPublicacao;
    private boolean disponivel;
    private int numeroEdicao;

    public Livro(String titulo, String autor, int anoPublicacao, boolean disponivel) {
        setTitulo(titulo);
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.disponivel = disponivel;
    }

    public String getAutor() {
        return autor;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public void setTitulo(String titulo) {
        this.setTitulo(titulo, 1);
    }

    public void setTitulo(String titulo, int numeroEdicao) {
        super.setTitulo(titulo);
        this.numeroEdicao = numeroEdicao;
    }

    public void setDetalhes(String titulo, String autor, int anoPublicacao) {
        setTitulo(titulo);
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
    }
    public boolean Disponivel() {
        return disponivel;
    }
    @Override
    public String detalhesDoProduto() {
        String disponibilidade = disponivel ? "Disponível" : "Indisponível";
        return "\nTitulo: " + getTitulo() + "\nAutor: " + autor + "\nAno de Publicação: " + anoPublicacao + "\nNúmero de Edição: " + numeroEdicao + "\nDisponibilidade: " + disponibilidade;
    }
}
