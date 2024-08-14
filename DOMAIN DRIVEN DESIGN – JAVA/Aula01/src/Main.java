import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // 2
        List<Double> numbers = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite 5 numeros");
        for (int i = 0; i < 5; i++) {
            double n1 = scanner.nextDouble();
            numbers.add(n1);
        }

        Calculos calculos = new Calculos(numbers);
        double media = calculos.media();
        System.out.println(media);

        // 3

        System.out.println("Type your balance: ");
        double balance = scanner.nextDouble();
        balance += balance * 0.01;
        System.out.println("Balance with reajust of 1%:  " +  balance);

        //4

        System.out.println("Type a int number");
        int number = scanner.nextInt();
        System.out.println(number - 1);
        System.out.println(number);
        System.out.println(number + 1);

        //5

        System.out.println("Qual é o salario mínimo? ");
        double salarioMinimo = scanner.nextDouble();
        System.out.println("Qual é o seu salario? ");
        double salario = scanner.nextDouble();

        double qntSalarioMinimo = salario / salarioMinimo;
        System.out.println(qntSalarioMinimo);


    }
}
