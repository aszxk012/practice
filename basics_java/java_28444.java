/* 28444
 * H * I = 첫번째 항
 * A * R * C = 두번째 항
 * HI - ARC 출력하기
 */

import java.util.Scanner;
public class java_28444 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int h = scanner.nextInt();
        int i = scanner.nextInt();

        int a = scanner.nextInt();
        int r = scanner.nextInt();
        int c = scanner.nextInt();

        int hi = h * i;
        int arc = a * r * c;

        System.out.println(hi - arc);
        scanner.close();
    }
}
