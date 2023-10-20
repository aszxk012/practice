/* 3007
 * 라면 끓이는 횟수 N이 주어지고 라면의 물 양 구하기
 * W = A(X - 1) + B
 */

import java.util.*;
public class java_30007 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int x = scanner.nextInt();
            int w = a * (x - 1) + b;

            System.out.println(w);
        }

        scanner.close();
    }
}
