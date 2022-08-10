public abstract class Member implements PostarMensagem{
    private final String name;
    private final String email;
    private final FunctionsEnum function;
    private boolean isOnExtraHour;
    public Member(String name, String email, FunctionsEnum function, boolean isOnExtraHour) {
        this.name = name;
        this.email = email;
        this.function = function;
        this.isOnExtraHour = isOnExtraHour;
    }
    public String getName() {
        return name;
    }
    public String getEmail() {
        return email;
    }
    public FunctionsEnum getFunction() {
        return function;
    }
    public boolean getIsOnExtraHour() {
        return isOnExtraHour;
    }
    protected void setIsOnExtraHour(boolean isOnExtraHour){
        this.isOnExtraHour = !isOnExtraHour;
    }
    @Override
    public String toString() {
        return "Member [email=" + email + ", function=" + function + ", isOnExtraHour=" + isOnExtraHour + ", name="
                + name + "]";
    }
}