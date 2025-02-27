import models.Address;
import models.Person;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        //        List<String> strings = new ArrayList<>();
//        strings.add("teste1");
//        strings.add("teste2");
//        strings.forEach(System.out::println);
//
//        for (String texto : strings) {
//            System.out.println(texto);
//        }

        List<Address> enderecos = new ArrayList<>();
        enderecos.add(new Address("rua trajano", 100, 33131, "residencial"));
        enderecos.add(new Address("rua flores", 200, 212123, "comercial"));

        List<Person> personList = new ArrayList<>();
        personList.add( new Person("Leando", 50, "doc", enderecos));
        personList.add( new Person("Roberto", 10, "doc", enderecos));
        personList.add( new Person("Marcos", 70, "doc", enderecos));
        personList.forEach(System.out::println);


        Set<Integer> integers = new HashSet<>(); // Não aceita valores iguais. Deixa na ordem os valores
        integers.add(1);
        integers.add(5);
        integers.add(3);
        integers.forEach(System.out::println);

    }
}