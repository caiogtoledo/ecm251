// Caio Toledo 20.01430-9
public class Bicycle extends Vehicle{
    
    public Bicycle(float costPerHour){
        super(costPerHour);
    }

    @Override
    public EnumVehicleTypes getType() {
        return EnumVehicleTypes.BICYCLE;
    }
}
