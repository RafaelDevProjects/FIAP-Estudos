package org.example.models;

import java.util.List;

public class Cardapio {
    private List<Prato> pratos;
    private List<Bebida> bebidas;

    public Cardapio(List<Prato> pratos, List<Bebida> bebidas) {
        this.pratos = pratos;
        this.bebidas = bebidas;
    }

    public List<Prato> getPratos() {
        return pratos;
    }

    public void setPratos(List<Prato> pratos) {
        this.pratos = pratos;
    }

    public List<Bebida> getBebidas() {
        return bebidas;
    }

    public void setBebidas(List<Bebida> bebidas) {
        this.bebidas = bebidas;
    }
}
