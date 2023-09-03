public class aluno {
    prova prova1;
    prova prova2;
    double CalcularMedia(){
        double media = (prova1.calcularNotaTotal() + prova2.calcularNotaTotal()) / 2;
        return media;
    }
}
