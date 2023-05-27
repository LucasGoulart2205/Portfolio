 class Main {
    public static void main(String[] args) {

        //Primeira gincana

        Estudante estudante1 = new Estudante();
        estudante1.setNome("Lucas Goulart");
        estudante1.setIdade(18);
        estudante1.setPontos(999);

        Estudante estudante2 = new Estudante();
        estudante2.setNome("Cristiano Ronaldo");
        estudante2.setIdade(38);
        estudante2.setPontos(790);

        Estudante estudante3 = new Estudante();
        estudante3.setNome("Lionel Messi");
        estudante3.setIdade(35);
        estudante3.setPontos(800);

        Gincana gincana1 = new Gincana();
        gincana1.setNomeGincana("Gincana de Futebol: ");
        System.out.println("\n" + gincana1.getNomeGincana());
        gincana1.adicionarEstudante(estudante1);
        gincana1.adicionarEstudante(estudante2);
        gincana1.adicionarEstudante(estudante3);
        gincana1.exibirVencedor();

        //Segunda gincana

        Estudante estudante4 = new Estudante();
        estudante4.setNome("Lucas Goulart");
        estudante4.setIdade(30);
        estudante4.setPontos(999);

        Estudante estudante5 = new Estudante();
        estudante5.setNome("Bill Gates + Elon Musk");
        estudante5.setIdade(118);
        estudante5.setPontos(998);

        Gincana gincana2 = new Gincana();
        gincana2.setNomeGincana("Gincana de Programação: ");
        System.out.println("\n" + gincana2.getNomeGincana());
        gincana2.adicionarEstudante(estudante4);
        gincana2.adicionarEstudante(estudante5);
        gincana2.exibirVencedor();
    }
}
