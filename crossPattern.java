import java.util.*;

public class patterns {
    public static void main(String argc[]) {
        int b = 1;
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        for (int i = 1; i <=2*a; i++) {
            for (int j = 1; j <=2*a; j++) {
                if (i==j || i+j==2*a+1) {
                    System.out.print("  ");
                }
                else
                System.out.print(" *");
            }
            System.out.println("");
        }

    }

}
