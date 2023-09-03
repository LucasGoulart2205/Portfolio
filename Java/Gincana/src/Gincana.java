public class Gincana {
    private String nomeGincana;
    private int totalEstudantes;
    private Estudante estudanteVencedor;
    private int pontuacaoMaxima;

    //nome gincana
    public void setNomeGincana(String nomeGincana){
        this.nomeGincana = nomeGincana;
    }
    public String getNomeGincana(){
        return  this.nomeGincana;
    }

    //total estudantes
    public int getTotalEstudantes(){
        return this.totalEstudantes;
    }
    public void setTotalEstudantes(int totalEstudantes){
        this.totalEstudantes = totalEstudantes;
    }
    //estudante vencedor
    public Estudante getEstudanteVencedor(){
        return estudanteVencedor;
    }

    public void setEstudanteVencedor(Estudante estudanteVencedor){
        this.estudanteVencedor = estudanteVencedor;
    }
    //pontuacao maxima
    public int getPontuacaoMaxima(){
        return pontuacaoMaxima;
    }
    public void setPontuacaoMaxima(int pontuacaoMaxima){
        this.pontuacaoMaxima = pontuacaoMaxima;
    }
    public void adicionarEstudante (Estudante estudante){
        totalEstudantes++;
        if (estudanteVencedor == null || estudante.getPontos() > estudanteVencedor.getPontos()){
            estudanteVencedor = estudante;
            pontuacaoMaxima = estudante.getPontos();
        }
    }

    public void exibirVencedor(){
        System.out.println("O vencedor da gincana é: " + estudanteVencedor.getNome());
        System.out.println("Com uma pontção de: " + estudanteVencedor.getPontos() + " pontos");
    }
}
