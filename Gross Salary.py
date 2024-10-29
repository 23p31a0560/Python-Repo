import java.util.Scanner;
public class gross
    {
        public static void main(String args[])
        {
            Scanner sc=new Scanner(System.in);
            int n=sc.nextInt();
            double DA,HRA;
            if(n<=10000)
            {
                DA=n*0.80;
                HRA=n*0.20;
                {
                    System.out.printf("%.2f",n+DA+HRA);
                }
            }
            else if(n<=20000)
            {
                DA=n*0.90;
                HRA=n*0.25;
                {
                    System.out.printf("%.2f",n+DA+HRA);
                }
            }
            else
            {
                DA=n*0.95;
                HRA=n*0.30;
                {
                    System.out.printf("%.2f",n+DA+HRA);
                }
            }
        }
    }
