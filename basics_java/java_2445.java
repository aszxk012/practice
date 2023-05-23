/* 2445
 * 별 찍기
 */

import java.util.*;
 public class java_2445 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        for (int i = 1; i <= num; i++){
            for (int j = 1; j <= i; j++){
                System.out.print("*");
            }

            for (int k = 1; k <= 2 * (num - i); k++){
                System.out.print(" ");
            }

            for (int l = 1; l <= i; l++){
                System.out.print("*");
            }

            System.out.println();
        }

        for (int i = num - 1; i >= 1; i--){
            for (int j = i; j >= 1; j--){
                System.out.print("*");
            }

            for (int k = 2 * (num - i); k >= 1; k--){
                System.out.print(" ");
            }

            for (int l = i; l >= 1; l--){
                System.out.print("*");
            }

            System.out.println();
        }
        scanner.close();
    }
}
