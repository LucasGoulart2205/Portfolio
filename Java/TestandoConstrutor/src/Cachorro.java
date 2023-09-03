public class Cachorro {
    private String nome;
    private String raca;
    private int idade;

    public Cachorro(String nome, String raca, int idade){
        this.nome = nome;
        this.raca = raca;
        this.idade = idade;
    }
    public Cachorro(String nome, String raca){
        this.nome = nome;
        this.raca = raca;
        this.idade = 32;
    }
    public void imprimir(){
        System.out.println("\n" + "Nome: " + this.nome);
        System.out.println("raça: " + this.raca);
        System.out.println("idade: " + this.idade);
    }
    public static void main(String[] args) {
        Cachorro cachorro1 = new Cachorro("Rex", "Pitbull");
        cachorro1.imprimir();
        Cachorro cachorro2 = new Cachorro("Lucas Goulart", "Pincher", 10);
        cachorro2.imprimir();
    }
}
