import java.util.Scanner;
public class Simple
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int p=sc.nextInt();
        int r=sc.nextInt();
        int t=sc.nextInt();
        int res=(p*r*t)/100;
        System.out.println(res);
        sc.close();
    }
}