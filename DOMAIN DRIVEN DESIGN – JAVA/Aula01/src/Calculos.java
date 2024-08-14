import java.util.ArrayList;
import java.util.List;

public class Calculos {
    private List<Double> numbers = new ArrayList<>();
    private double media;

    public Calculos (List<Double> numbers){
        this.numbers.addAll(numbers);
        this.media = media();
    }

    public double soma () {
        double soma = 0.0;
        for (int i = 0; i < numbers.size(); i++) {
            soma += numbers.get(i);
        }
        return soma;
    }

    public double media(){
        return soma() / numbers.size();

    }
}
