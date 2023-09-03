public class Equipe {
    private String nome;
    private int vitorias;
    private int derrotas;
    private int empates;
    private int pontos;
    private int kills;

    public Equipe(String nome, int vitorias, int derrotas, int empates){
        this.nome = nome;
        this.vitorias = 0;
        this.derrotas = 0;
        this.empates = 0;
    }

    public int getPontos() {
        return pontos;
    }

    public void setPontos(int pontos) {
        this.pontos = pontos;
    }

    public Equipe() {

    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getVitorias() {
        return vitorias;
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }
    public void registrarVitoria(int kills){
        this.vitorias ++;
        this.pontos += 3;
        this.kills = this.kills + kills;
    }
    public void registrarDerrota(int kills){
        this.derrotas ++;
        this.kills = this.kills + kills;
    }
    public void registrarEmpate(int kills){
        this.empates ++;
        this.pontos ++;
        this.kills = this.kills + kills;
    }

    public double calcularfuncoes(){
        int totaldejogos = this.derrotas + this.vitorias + this.empates;
        int totaldepontospossiveis = totaldejogos * 3;
        double aproveitamento = 0;
        if(totaldepontospossiveis > 0){
            aproveitamento = (double) pontos / totaldepontospossiveis * 100;
        }
        return aproveitamento;
    }


    public void exibirinfo(){
        System.out.println("\n•Equipe: " + this.nome);
        System.out.println("Vitorias: " + this.vitorias);
        System.out.println("Derrotas: " + this.derrotas);
        System.out.println("Empates: " + this.empates);
        System.out.println("Pontos:" + this.pontos);
        System.out.println("Aproveitamento: " + this.calcularfuncoes());
        System.out.println("Kills: " + this.kills);
    }


}
