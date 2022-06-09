public class BigBrothers extends Member{

    public BigBrothers(String name, String email, boolean isOnExtraHour) {
        super(name, email, FunctionsEnum.BBB, isOnExtraHour);
    }

    @Override
    public void showMessage(Member member) {
        System.out.println(member.getName()+" (" +member.getFunction()+ ") "+ ":");
        if(member.getIsOnExtraHour()){
            System.out.println("...");
        }else{
            System.out.println("Sempre ajudando as pessoas membros ou não S2!");
        } 
    }
}
