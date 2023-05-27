public class Main {
    public static void main(String[] args) {
        turma turma = new turma();

        aluno aluno1 = new aluno();
        aluno aluno2 = new aluno();
        aluno aluno3 = new aluno();

        turma.aluno1 = aluno1;
        turma.aluno2 = aluno2;
        turma.aluno3 = aluno3;

        prova aluno1prova1 = new prova();
        aluno1prova1.notaParte1 = 4.0;
        aluno1prova1.notaParte2 = 2.5;
        aluno1.prova1 = aluno1prova1;

        prova aluno1prova2 = new prova();
        aluno1prova2.notaParte1 = 1.0;
        aluno1prova2.notaParte2 = 7.0;
        aluno1.prova2 = aluno1prova2;
        ///aluno2
        prova aluno2prova1 = new prova();
        aluno2prova1.notaParte1 = 6.5;
        aluno2prova1.notaParte2 = 3.5;
        aluno2.prova1 = aluno2prova1;

        prova aluno2prova2 = new prova();
        aluno2prova2.notaParte1 = 0.0;
        aluno2prova2.notaParte2 = 3.0;
        aluno2.prova2 = aluno2prova2;

        //aluno 3
        prova aluno3prova1 = new prova();
        aluno3prova1.notaParte1 = 5.0;
        aluno3prova1.notaParte2 = 4.0;
        aluno3.prova1 = aluno3prova1;

        prova aluno3prova2 = new prova();
        aluno3prova2.notaParte1 = 6.0;
        aluno3prova2.notaParte2 = 1.5;
        aluno3.prova2 = aluno3prova2;

        System.out.println("Media aluno 1" + turma.aluno1.CalcularMedia());
        System.out.println("Media aluno 2" + turma.aluno2.CalcularMedia());
        System.out.println("Media aluno 3" + turma.aluno3.CalcularMedia());

        System.out.println("Media da turma" + turma.CalcularMedia());




    }
}
