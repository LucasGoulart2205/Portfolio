import java.util.Scanner;

public class atividade4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite um número: ");
        int numero = sc.nextInt();
        int i = 1;
        while (i <= numero) {
            if (i % 2 == 0) {
                System.out.println(i);
            }
            i++;
        }
    }
}
