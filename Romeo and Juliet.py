import java.util.Scanner;
public class Romeo
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x,y,z;
        x=sc.nextInt();
        y=sc.nextInt();
        z=sc.nextInt();
        int tot=5*x+10*y;
        int cho=(tot)/z;
        System.out.println(cho);
        sc.close();
    }
}