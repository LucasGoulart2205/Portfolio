import java.util.Scanner;

public class atividade1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite um numero: ");
        int numero = sc.nextInt();
        int i = 1;
        int soma = 0;
        while (i <= numero){
            soma += i;
            i++;
        }
        System.out.println("A soma dos numeros até: " + numero + " é " + soma);
    }

}
