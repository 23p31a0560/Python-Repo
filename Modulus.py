import java.util.Scanner;
public class Mod
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n1=sc.nextInt();
        int n2=sc.nextInt();
        int res=n1%n2;
        System.out.println(res);
        sc.close();
    }
}