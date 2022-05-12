// Caio Toledo 20.01430-9
public class User {
    private String name;
    private Vehicle vehicle;
    public int counter;

    public User(String name){
        this.setName(name);
        this.counter = 0;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Vehicle getVehicle() {
        return vehicle;
    }

    public void setVehicle(Vehicle vehicle) {
        this.counter += 1;
        this.vehicle = vehicle;
    }

    public void test(){
        System.out.println("---------------------");
        System.out.println("Quantidade de bens já compartilhados: " + counter);
        System.out.println("ID do veículo: " + vehicle.getId());
        System.out.println("Custo por hora: " + vehicle.getCostPerHour());
        System.out.println("---------------------");
    }
}
