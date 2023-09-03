public class Estudante {
    private String nome;
    private String matricula;
    private String curso;
    public Estudante(String nome, String matricula, String curso){
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
    }
    public Estudante(String nome, String matricula){
        this.nome = nome;
        this.matricula = matricula;
        this.curso = "Medicina";
    }

    public void imprimir(){
        System.out.println("\n" + "Nome: " + this.nome);
        System.out.println("Matricula: " + this.matricula);
        System.out.println("Curso: " + this.curso);
    }

    public static void main(String[] args) {
        Estudante estudante1 = new Estudante("Lucas","XXX", "Informatica");
        Estudante estudante2 = new Estudante("Larissa", "YYY");
        estudante1.imprimir();
        estudante2.imprimir();
    }
}
