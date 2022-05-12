public class Car extends Vehicle{
    
    public Car(float costPerHour){
        super(costPerHour);
    }

    @Override
    public EnumVehicleTypes getType() {
        return EnumVehicleTypes.CAR;
    }
}
