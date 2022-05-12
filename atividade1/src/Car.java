// Caio Toledo 20.01430-9
public class Car extends Vehicle{
    
    public Car(float costPerHour){
        super(costPerHour);
    }

    @Override
    public EnumVehicleTypes getType() {
        return EnumVehicleTypes.CAR;
    }
}
