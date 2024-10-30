import java.util.Scanner;
public class Value
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        double s=x*(9.0/5.0)+32;
        System.out.printf("%.2f",s);
    }
}