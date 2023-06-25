/* 19602
 * S, M, L은 간식의 크기
 * 행복 = 1 * S + 2 * M + 3 * L 
 * 10 이상이면 happy, 미만이면 sad 출력하기
 */

import java.util.*;
public class java_19602 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int s = scanner.nextInt();
        int m = scanner.nextInt();
        int l = scanner.nextInt();
        int sum = (1 * s) + (2 * m) + (3 * l);

        if (sum >= 10) {
            System.out.println("happy");
        }
        else {
            System.out.println("sad");
        }
        scanner.close();
    }
}
