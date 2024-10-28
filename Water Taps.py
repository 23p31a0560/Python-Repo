import java.util.Scanner;
public class Time
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        int res=(x*y)/(x+y);
        System.out.println(res);
        sc.close();
    }
}