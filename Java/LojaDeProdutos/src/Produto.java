public class Produto {
    private String nome;
    private double Preco;
    private int Quantidade;

    public int getQuantidade(){
        return  this.Quantidade;
    }

    public void setQuantidade(int Quantidade){
        if(Quantidade < 0){
            System.out.println("Quantidade nao pode ser menor que zero");
        }else {
            this.Quantidade = Quantidade;
        }
    }

    public void setNome(String nome){
        this.nome = nome;
    }
    public String getNome(){
        return this.nome;
    }
    public double getPreco(){
        return this.Preco;
    }
    public void setPreco(double preco){
        this.Preco = preco;
    }

}
