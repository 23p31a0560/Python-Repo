import java.util.Scanner;
public class Car
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        for(int i=0;i<n;i++)
        {
            int x1=sc.nextInt();
            int x2=sc.nextInt();
            int y1=sc.nextInt();
            int y2=sc.nextInt();
            double car1=(double)y1/x1;
            double car2=(double)y2/x2;
            if(car1<car2)
            {
                System.out.println(-1);
            }
            else if(car1==car2)
            {
                System.out.println(0);
            }
            else{
                System.out.println(1);
            }

        }
    }
}