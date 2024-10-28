import java.util.Scanner;
public class Convert
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int H=x/3600;
        int rs=x%3600;
        int M=rs/60;
        int s=rs%60;
        System.out.println("H:M:S-"+H+":"+M+":"+s);
        sc.close();
    }
}