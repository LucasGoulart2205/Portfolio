public class Livro {
    private String titulo;
    private String autor;
    private double preco;

    public Livro(String titulo, String autor, double preco){
        this.titulo = titulo;
        this.autor = autor;
        this.preco = preco;
    }
    public Livro(String titulo, String autor){
        this.titulo = titulo;
        this.autor = autor;
        this.preco = 29.99;
    }
    public void imprimir(){
        System.out.println("\n" +"Titulo: " + this.titulo);
        System.out.println("Autor: " + this.autor);
        System.out.println("Preço: " + this.preco);
    }

    public static void main(String[] args) {
        Livro livro1 = new Livro("Outsider", "Stephen King", 50);
        livro1.imprimir();
        Livro livro2 = new Livro("Naruto", "Kishimoto");
        livro2.imprimir();
    }

}
