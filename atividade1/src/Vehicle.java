// Caio Toledo 20.01430-9
import java.util.concurrent.ThreadLocalRandom;

public class Vehicle {
    private int id;
    private float costPerHour;

    public Vehicle(float costPerHour){
        this.setId(generateId());
        this.setCostPerHour(costPerHour);
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public float getCostPerHour() {
        return costPerHour;
    }

    public void setCostPerHour(float costPerHour) {
        this.costPerHour = costPerHour;
    }

    static int generateId(){
        String id = "";
        for (int i = 0; i < 5; i++) {
            id = id + ThreadLocalRandom.current().nextInt(1,11);
        }
        return Integer.parseInt(id);
    }

    public EnumVehicleTypes getType(){
        return EnumVehicleTypes.CARRO;
    }
}
