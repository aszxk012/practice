/* 1977
 * M과 N이 주어질 때 M이상, N이하의 자연수 중
 * 완전 제곱수인 것을 골라 합 구한 후 출력, 그 중 최솟값 출력하기
 */

import java.util.*;
public class java_1977 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        int sum = 0;
        int min = Integer.MAX_VALUE;

        for (int i = m; i <= n; i++) {
            int sq = i * i;
            if (sq <= n) {
                sum += sq;
                min = Math.min(min, i);
            }
        }

        System.out.println(sum);
        System.out.println(min);
        scanner.close();
    }
}