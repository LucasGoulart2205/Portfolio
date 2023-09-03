public class Main {
    public static void main(String[] args) {
        //Criando livros
        Livro livro1 = new Livro("Harry Potter", "J. K. Rowling", 1997, false);
        Livro livro2 = new Livro("O Senhor dos Anéis", "J. R. R. Tolkien", 1954, false);
        Livro livro3 = new Livro("Saga Crepúsculo", "Stephenie Meyer", 2005, true);

        //Detalhes dos livros
        System.out.println("\n•Livro 1" + livro1.detalhesDoProduto());
        System.out.println("\n•Livro 2: " + livro2.detalhesDoProduto());
        System.out.println("\n•Livro 3: " + livro3.detalhesDoProduto());

        //Acessando Autores
        System.out.println("\n•Autores abaixo: ");
        System.out.println("Autor do Livro 1: " + livro1.getAutor());
        System.out.println("Autor do Livro 3: " + livro3.getAutor());

        //Acessando ano de publicacao
        System.out.println("\n•Anos de publicação abaixo: ");
        System.out.println("Ano de Publicação do Livro 2: " + livro2.getAnoPublicacao());
        System.out.println("Ano de Publicação do Livro 3: " + livro3.getAnoPublicacao());

        //Atualizando detalhes de um livro
        System.out.println("\n•Alterações realizadas: ");
        livro1.setTitulo("Harry Potter: A Câmara Secreta", 2);
        System.out.println("Livro 1 Atualizado: " + livro1.detalhesDoProduto());

        //Criando biblioteca
        Biblioteca biblioteca = new Biblioteca();

        //Adicionando livros à biblioteca
        biblioteca.adicionarLivro(livro1);
        biblioteca.adicionarLivro(livro2);
        biblioteca.adicionarLivro(livro3);

        //Verificando se o livro esta disponivel
        System.out.println("\n•Verificando se estão disponiveis: ");
        System.out.println("Disponibilidade do Livro 1: " + biblioteca.verificarDisponibilidadeLivro(livro1));
        System.out.println("Disponibilidade do Livro 2: " + biblioteca.verificarDisponibilidadeLivro(livro2));
        System.out.println("Disponibilidade do Livro 3: " + biblioteca.verificarDisponibilidadeLivro(livro3));

        //Removendo um livro da biblioteca
        biblioteca.removerLivro(livro2);

        //Adicionando um novo livro à biblioteca
        System.out.println("\n•Novo livro adicionado: ");
        Livro livro4 = new Livro("O Diário de Anne Frank", "Anne Frank", 1947, true);
        biblioteca.adicionarLivro(livro4);
        System.out.println("Livro 4: " + livro4.detalhesDoProduto());

        //Atualizando detalhes de um livro na biblioteca
        System.out.println("\n•Atualizando detalhes do livro: ");
        biblioteca.atualizarDetalhesLivro(livro2, "O Senhor dos Anéis: A vingança", "J. R. R. Tolkien", 2018);
        System.out.println("Livro 2: " + livro2.detalhesDoProduto());

        //Removendo um livro da biblioteca
        biblioteca.removerLivro(livro3);
    }
}
