package models;
import java.util.ArrayList;
import java.util.List;

public class Person {
    private String name;
    private int age;
    private String documents;
    private List<Address> enderecos = new ArrayList<>();

    public Person(String name, int age, String documents, List<Address> endereco) {
        this.name = name;
        this.age = age;
        this.documents = documents;
        this.enderecos.addAll(endereco);
    }

    public Person(String name, int age, String documents) {
        this.name = name;
        this.age = age;
        this.documents = documents;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getDocuments() {
        return documents;
    }

    public void setDocuments(String documents) {
        this.documents = documents;
    }


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("name = " )
                .append(name)
                .append(", idade = ")
                .append(age)
                .append(", documentos = ")
                .append(documents)
                .append(enderecos);
        return sb.toString();
    }
}
