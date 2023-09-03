public class turma {
    aluno aluno1;
    aluno aluno2;
    aluno aluno3;

    double CalcularMedia(){
        double mediaTurma = (aluno1.CalcularMedia() + aluno2.CalcularMedia() + aluno3.CalcularMedia()) / 3;
        return mediaTurma;
    }
    }

