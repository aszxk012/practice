/* 17256
 * a(x, y z) (cake) b(x, y, z) = 
 * (a.z + b.x, a.y * b.y, a.x + b.z) =
 * c(x, y, z)
 * 일 때, a와 c가 주어진다. 위의 식이 성립하도록 b 구하여 출력하기
 */

import java.util.Scanner;
public class java_17256 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int a_x = scanner.nextInt();
        int a_y = scanner.nextInt();
        int a_z = scanner.nextInt();

        int c_x = scanner.nextInt();
        int c_y = scanner.nextInt();
        int c_z = scanner.nextInt();

        int b_x = c_x - a_z;
        int b_y = c_y / a_y;
        int b_z = c_z - a_x;

        System.out.printf("%d ", b_x);
        System.out.printf("%d ", b_y);
        System.out.printf("%d", b_z);
        scanner.close();
    }
}
