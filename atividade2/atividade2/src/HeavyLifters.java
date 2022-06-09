public class HeavyLifters extends Member{

    public HeavyLifters(String name, String email, boolean isOnExtraHour) {
        super(name, email, FunctionsEnum.HEAVY, isOnExtraHour);
    }

    @Override
    public void showMessage(Member member) {
        System.out.println(member.getName()+" (" +member.getFunction()+ ") "+ ":");
        if(member.getIsOnExtraHour()){
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        }else{
            System.out.println("Podem contar conosco!");
        }
    }
    
}
