import java.util.Scanner;
public class Rupee
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int r=4*x;
        if(r<1000)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
    }
}