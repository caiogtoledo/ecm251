public class MobileMembers extends Member{

    public MobileMembers(String name, String email, boolean isOnExtraHour) {
        super(name, email, FunctionsEnum.MOBILE, isOnExtraHour);
    }

    @Override
    public void showMessage(Member member) {
        System.out.println(member.getName()+" (" +member.getFunction()+ ") "+ ":");
        if(member.getIsOnExtraHour()){
            System.out.println("Happy_C0d1ng. Maskers");
        }else{
            System.out.println("Happy Coding!");
        }
    }

}
