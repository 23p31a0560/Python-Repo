import java.util.Scanner;
public class Marks
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int py=sc.nextInt();
        int chem=sc.nextInt();
        int bio=sc.nextInt();
        int math=sc.nextInt();
        int com=sc.nextInt();
        int n=py+chem+bio+math+com;
        double per=(n/5.0);
        if(per>=90)
        {
            System.out.println("Grade A");
        }
        else if(per>=80)
        {
            System.out.println("Grade B");
        }
        else if(per>=70)
        {
            System.out.println("Grade C");
        }
        else if(per>=60)
        {
            System.out.println("Grade D");
        }
        else if(per>=40)
        {
            System.out.println("Grade E");
        }
        else if(per<40)
        {
            System.out.println("Grade F");
        }
    }
}