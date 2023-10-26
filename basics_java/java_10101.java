/* 10101
 * 세 각의 크기가 60이면 Equilateral
 * 세 각의 합이 180이고 두 각이 같다면 Isosceles
 * 세 각의 합이 180이고 같은 각이 없다면 Scalene
 * 세 각의 합이 180이 아니면 Error
 */

import java.util.Scanner;
public class java_10101 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int sum = a + b + c;

        if ((a == b) & (b == c) & (c == a) & (a == 60)) {
            System.out.print("Equilateral");
        }
        else if (sum == 180) {
            if ((a == b) | (b == c) | (a == c)) {
                System.out.print("Isosceles");
            }

            else {
                System.out.print("Scalene");
            }
        } 

        else if (sum != 180) {
            System.out.print("Error");
        }
        
        scanner.close();
    }
}
