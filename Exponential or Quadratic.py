import java.util.Scanner;
public class Hold
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        if(n>=5)
        {
            System.out.println("Yes");
        }
        else
        {
            if(n==1)
            {
            System.out.println("Yes");
            }
            else if(n==2 || n==3 || n==4 )
            {
                System.out.println("No");
            }
        }
    }
}