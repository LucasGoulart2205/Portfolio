public class Main {
    public static void main(String[] args) {
        Quadrado quadrado = new Quadrado();
        quadrado.lado = 4;
        double resultado1 = quadrado.CalcularArea();
        System.out.println(resultado1);

        Circunferencia circunferencia = new Circunferencia();
        circunferencia.raio=3;
        double resultado2 = circunferencia.CalcularCircunferencia();
        System.out.println(resultado2);

        Trapezio trapezio = new Trapezio();
        trapezio.baseMaior= 2;
        trapezio.baseMenor=2;
        trapezio.altura= 3;
        double resultado3 = trapezio.CalcularTrapezio();
        System.out.println(resultado3);

        Triangulo triangulo = new Triangulo();
        triangulo.altura= 3;
        triangulo.base= 4;
        double resultado4 = triangulo.CalcularTriangulo();
        System.out.println(resultado4);
    }
}