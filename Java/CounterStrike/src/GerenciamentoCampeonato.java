public class GerenciamentoCampeonato {
    public static void main(String[] args) {
        Equipe equipe1 = new Equipe();
        equipe1.setNome("Loud");
        equipe1.registrarVitoria(3);
        equipe1.registrarDerrota(2);
        equipe1.registrarEmpate(1);


        Equipe equipe2 = new Equipe();
        equipe2.setNome("Furia");
        equipe2.registrarVitoria(3);
        equipe2.registrarVitoria(2);
        equipe2.registrarDerrota(7);
        equipe2.registrarEmpate(5);
        equipe2.registrarEmpate(4);

        equipe1.exibirinfo();
        equipe2.exibirinfo();



    }
}
