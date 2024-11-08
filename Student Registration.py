import java.util.Scanner;
public class Friends
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        
        int n=sc.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++)
         {
         int t=sc.nextInt();
         int m=sc.nextInt();
         int k=sc.nextInt();
         if(m>=t+k)
         {
            System.out.println("YES");

         }
         else
         {
            System.out.println("NO");
         }
         }


    }
}