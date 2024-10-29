import java.util.Scanner;
public class Pavan
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x1=sc.nextInt();
        int y1=sc.nextInt();
        int x2=sc.nextInt();
        int y2=sc.nextInt();
        int f1=x1+y1;
        int f2=x2+y2;
        if(f1<f2)
        {
            System.out.println(f1);
        }
        else
        {
            System.out.println(f2);
        }
    }
}