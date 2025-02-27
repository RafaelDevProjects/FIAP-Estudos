package org.example.models;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Cardapio {

    private Map<Integer, Prato> pratos;

    private Map<Integer, Bebida> bebidas;

    public Cardapio(Map<Integer, Prato> pratos, Map<Integer, Bebida> bebidas) {
        this.pratos = carregarPratos();
        this.bebidas = carregarBebidas();
    }

    public Cardapio() {
    }

    public Map<Integer, Prato> getPratos() {
        return pratos;
    }

    public void setPratos(Map<Integer, Prato> pratos) {
        this.pratos = pratos;
    }

    public Map<Integer, Bebida> getBebidas() {
        return bebidas;
    }

    public void setBebidas(Map<Integer, Bebida> bebidas) {
        this.bebidas = bebidas;
    }

    public Map<Integer, Prato> carregarPratos() {
        Map<Integer, Prato> pratos = new HashMap<Integer, Prato>();

        Prato prato = new Prato(1, "baiao de dois", "Arroz, feijão, queijo qualho, coentro", 50.f);
        Prato prato1 = new Prato(1, "Da casa", "Carne moida com batata", 30.f);
        Prato prato2 = new Prato(1, "Parmegiana", "File mingnon, arroz, fritas", 60.f);

        pratos.put(prato1.getCodigo(), prato1);
        pratos.put(prato.getCodigo(), prato);
        pratos.put(prato2.getCodigo(), prato2);

        return pratos;

    }

    public Map<Integer, Bebida> carregarBebidas() {
        Map<Integer, Bebida> bebidas = new HashMap<Integer, Bebida>();

        Bebida bebida = new Bebida(1, "Refrigerante", "Coca-cola, fanta", 8.f);
        Bebida bebida2 = new Bebida(2, "Agua", "Agua", 5.f);

        bebidas.put(bebida.getCodigo(), bebida);
        bebidas.put(bebida2.getCodigo(), bebida2);

        return bebidas;
    }

}
