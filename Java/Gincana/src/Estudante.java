public class Estudante {
    //Atributos
    private String nome;
    private int idade;
    private int pontos;

    //Metodos (Get e set);
    //Nome;
    public void setNome(String nome){
        this.nome = nome;
    }
    public String getNome(){
        return this.nome;
    };

    //idade
    public int getIdade(){
        return this.idade;
    }
    public void setIdade(int idade){
        if(idade <= 0){
            System.out.println("Erro ao digitar idade");
        }else{
            this.idade = idade;
        }
    }

    //pontos
    public int getPontos(){
        return this.pontos;
    }

    public void setPontos(int pontos){
        this.pontos = pontos;
    }

}
