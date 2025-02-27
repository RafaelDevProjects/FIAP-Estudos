package models;

public class Bebida {
    private int codigo;

    private String nome;

    private String descricao;

    private float valor;

    public Bebida(int codigo, String nome, String descricao, float valor) {
        super();
        this.codigo = codigo;
        this.nome = nome;
        this.descricao = descricao;
        this.valor = valor;
    }

    @Override
    public String toString() {
        return "Código: " + this.codigo + " Bebida " + this.nome + " Descricao " + this.descricao + "-----" + " Preço " + this.valor;
    }

    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public float getValor() {
        return valor;
    }

    public void setValor(float valor) {
        this.valor = valor;
    }


}
