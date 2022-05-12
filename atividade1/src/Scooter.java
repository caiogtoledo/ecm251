public class Scooter extends Vehicle{
    
    public Scooter(float costPerHour){
        super(costPerHour);
    }

    @Override
    public EnumVehicleTypes getType() {
        return EnumVehicleTypes.SCOOTER;
    }
}
