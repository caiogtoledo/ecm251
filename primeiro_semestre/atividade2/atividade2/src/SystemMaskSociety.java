import java.util.ArrayList;
import java.util.List;

public class SystemMaskSociety {
    public static void run(){
        System.out.println("========================================");
        System.out.println("Seja bem vindo ao Sistema Mask Society");
        System.out.println("========================================");

        List<Member> members = new ArrayList<Member>();

        members.add(new MobileMembers(
            "Caio", 
            "caio@email.com", 
            false)
        );

        members.add(new HeavyLifters(
            "Bruno", 
            "bruno@email.com", 
            false)
        );

        members.add(new ScriptGuys(
            "Luca", 
            "luca@email.com", 
            false)
        );

        members.add(new BigBrothers(
            "Flavio", 
            "flavio@email.com", 
            false)
        );

        showAllMessages(members);

        changeWorkShift(members);

        showAllMessages(members);

        changeWorkShift(members);

        removeTypeMember(members, FunctionsEnum.HEAVY);
        removeTypeMember(members, FunctionsEnum.SCRIPT);

        showMembers(members);

        showAllMessages(members);

        System.out.println("=========================");
        System.out.println("Encerrando o sistema...");
        System.out.println("=========================");
    }

    public static void showMembers(List<Member> members){
        System.out.println("========================");
        System.out.println("Membros cadastrados...");
        System.out.println("========================");
        for(Member member : members){
            System.out.println(member);
        }
    }

    public static void changeWorkShift(List<Member> members){
        System.out.println("========================");
        System.out.println("TROCANDO DE TURNO...");
        System.out.println("========================");
        for (Member member : members){
            member.setIsOnExtraHour(member.getIsOnExtraHour());
        }
    }

    public static void showAllMessages(List<Member> members){
        System.out.println("========================");
        System.out.println("Mensagens:");
        System.out.println("========================");
        for (Member member : members){
            member.showMessage(member);
        }
    }

    public static void removeTypeMember(List<Member> members, FunctionsEnum function){
        for (Member member : members){
            if(member.getFunction() == function){
                members.remove(member);
                break;
            }
        }
    }
}
