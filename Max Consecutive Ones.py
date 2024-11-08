import java.util.Scanner;
public class Array
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++)
        {
           a[i] =sc.nextInt();
        }
        int maxcount=0;
        int cur=0;
        for(int i=0;i<n;i++)
        {
            if(a[i]==1)
            {
            cur++;
            }
            else
            {
                if(cur>maxcount)
                {
                    maxcount=cur;
                }
                cur=0;
            }
        }
        if(cur>maxcount)
        {
            maxcount=cur;

        }
        System.out.println(maxcount);

    }
}