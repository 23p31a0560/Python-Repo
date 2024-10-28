import java.util.Scanner;
public class Area
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        double s,Area;
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();
        s=(a+b+c)/2.0;
        Area=Math.sqrt(s*(s-a)*(s-b)*(s-c));
        System.out.printf("%.2f",Area);
        sc.close();
    }
}