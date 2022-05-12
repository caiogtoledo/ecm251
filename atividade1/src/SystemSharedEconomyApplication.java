public class SystemSharedEconomyApplication {
    public static void run() {
        Car car = new Car(100);
        Motorcycle motorcycle = new Motorcycle(90);
        Bicycle bicycle = new Bicycle(10);
        Scooter scooter = new Scooter(20);

        User user = new User("Caio");
        user.setVehicle(car);
        user.test();
        user.setVehicle(motorcycle);
        user.test();
        user.setVehicle(bicycle);
        user.test();
        user.setVehicle(scooter);
        user.test();
    }
}
