import java.util.Scanner;
public class Car
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int res=n/4;
        if(n%4==0)
        {
            System.out.println(res);
        }
        else
        {
            System.out.println(res+1);
        }
    }
}