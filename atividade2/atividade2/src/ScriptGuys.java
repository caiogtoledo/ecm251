public class ScriptGuys extends Member{

    public ScriptGuys(String name, String email, boolean isOnExtraHour) {
        super(name, email, FunctionsEnum.SCRIPT, isOnExtraHour);
    }

    @Override
    public void showMessage(Member member) {
        System.out.println(member.getName()+" (" +member.getFunction()+ ") "+ ":");
        if(member.getIsOnExtraHour()){
            System.out.println("QU3Ro_S3us_r3curs0s.py");
        }else{
            System.out.println("Prazer em ajudar novos amigos de código!");
        }  
    }
}
