package org.example;

import org.example.models.Bebida;
import org.example.models.Cardapio;
import org.example.models.Prato;

import java.util.Scanner;

public class Main {
    static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {

        try {
            Cardapio cardapio = new Cardapio();

            System.out.println("##### CARDAPIO #####");

            // Escolha prato
            cardapio.getPratos().values().forEach(System.out::println);
            System.out.println("Escolha seu prato: ");
            Prato prato = cardapio.getPratos().get(scanner.nextInt());
            System.out.println("O prato escolhido é: " + prato);

            // Escolha bebida
            cardapio.getPratos().values().forEach(System.out::println);
            System.out.println("Escolha sua bebida: ");
            Bebida bebida = cardapio.getBebidas().get(scanner.nextInt());
            System.out.println("A bebida escolhido é: " + bebida);

        } catch (Exception e){
            System.out.println("Erro: " + e.getMessage());
        }

    }
}