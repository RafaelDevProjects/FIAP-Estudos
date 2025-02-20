import java.sql.SQLOutput;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class TestQueue {
    public static void main(String[] args) {


        Queue<Integer> inteiros = new LinkedList<>(); // A saida sera igual a entrada
        inteiros.add(2);
        inteiros.add(3);
        inteiros.add(1);

        Queue<Integer> integers2 = new PriorityQueue<>(); // Coloca como prioridade a ordem, ou seja, a saida sera ordenada
        integers2.add(2);
        integers2.add(3);
        integers2.add(1);

        System.out.println("O elemento head é LinkedList: " + inteiros.peek()); // peak pega o primeiro que entrou
        System.out.println("O elemento head do PriorityQueue: " + integers2.peek());

        System.out.println("Queue com linkedList");
        inteiros.forEach(System.out::println);
        System.out.println("Queue com PriorityQueue");
        integers2.forEach(System.out::println);

    }
}
