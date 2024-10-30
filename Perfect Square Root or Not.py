import java.util.Scanner;
public class Square
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int sqrt=(int)Math.sqrt(n);
        if(n==sqrt*sqrt)
        {
            System.out.println("True");
        }
        else
        {
            System.out.println("False");
        }
        
    }
}