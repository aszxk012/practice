/* 1977
 * M과 N이 주어질 때 M이상, N이하의 자연수 중
 * 완전 제곱수인 것을 골라 합 구한 후 출력, 그 중 최솟값 출력하기
 * 최종 수정(2023.06.21)
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
            double sq = Math.sqrt((double) i);

            if (sq == (int) sq) {
                sum += i;
                min = Math.min(min, i);
            }
        }

        if(sum != 0) {
            System.out.println(sum);
            System.out.println(min);
        }
        else {
            System.out.println(-1);
        }
        scanner.close();
    }
}