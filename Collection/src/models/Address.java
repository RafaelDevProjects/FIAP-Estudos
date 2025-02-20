package models;

public class Address {
    private String street;
    private int number;
    private int cep;
    private String addressType;

    public Address(String street, int number, int cep, String addressType) {
        this.street = street;
        this.number = number;
        this.cep = cep;
        this.addressType = addressType;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public int getCep() {
        return cep;
    }

    public void setCep(int cep) {
        this.cep = cep;
    }

    public String getAddressType() {
        return addressType;
    }

    public void setAddressType(String addressType) {
        this.addressType = addressType;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(" Endereco = ")
                .append(", rua = ").append(street)
                .append(", numero = ").append(number)
                .append(", cep = ").append(cep)
                .append(", tipo de Endereço = ").append(addressType);
        return sb.toString();
    }
}
