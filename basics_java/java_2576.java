/* 2576
 * 7개의 자연수가 주어질 때, 홀수인 자연수를 골라 합을 구하고
 * 고른 홀수의 최솟값 구하기
 */

import java.util.*;
public class java_2576 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int min = Integer.MAX_VALUE;
        int sum = 0;

        for(int i = 0; i < 7; i++) {
            int num = scanner.nextInt();
            if (num % 2 != 0) {
                sum += num;
                min = Math.min(num, min);
            }
        }

        if (sum != 0) {
            System.out.println(sum);
            System.out.println(min);
        }
        else {
            System.out.println(-1);
        }
        scanner.close();
    }
}
