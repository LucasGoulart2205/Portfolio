public class Trapezio {
    double baseMaior;
    double baseMenor;
    double altura;

    double CalcularTrapezio(){
        System.out.println("\n•Calculo Trapezio: ");
        double area;
        area = ((baseMaior + baseMenor) / 2) * altura;
        return area;
    }
}
