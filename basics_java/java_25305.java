/* 25305
 * N명이 응시하고, K명이 상을 받는다.
 * 이때 상을 받는 커트라인 점수 출력하기
 */

import java.util.*;
public class java_25305 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int scores[] = new int[n];
        
        for (int i = 0; i < n; i++) {
            scores[i] = scanner.nextInt();
        }

        Arrays.sort(scores);
        // System.out.println(Arrays.toString(scores));
        System.out.println(scores[n - k]);

        scanner.close();
    }
}
