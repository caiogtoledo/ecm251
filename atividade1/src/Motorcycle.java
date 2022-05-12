public class Motorcycle extends Vehicle{
    
    public Motorcycle(float costPerHour){
        super(costPerHour);
    }

    @Override
    public EnumVehicleTypes getType() {
        return EnumVehicleTypes.MOTORCYCLE;
    }
}
