/* 10480
 * 입력 받은 수 짝수인지 홀수인지 판별하기
 */

import java.util.Scanner;
public class java_10480 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        for (int i = 0; i < num; i++) {
            int a = scanner.nextInt();

            if (a % 2 == 0) {
                System.out.println(a + " is even");
            }

            else {
                System.out.println(a + " is odd");
            }
        }
        scanner.close();
    }
}
