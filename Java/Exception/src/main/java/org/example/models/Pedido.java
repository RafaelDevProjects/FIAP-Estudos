package org.example.models;

import java.util.List;

public class Pedido {

    private int numMesa;

    private List<Prato> pratos;

    private List<Bebida> bebidas;

    public Pedido(int numMesa, List<Prato> pratos, List<Bebida> bebidas) {
        this.numMesa = numMesa;
        this.pratos = pratos;
        this.bebidas = bebidas;
    }

    public int getNumMesa() {
        return numMesa;
    }

    public void setNumMesa(int numMesa) {
        this.numMesa = numMesa;
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

