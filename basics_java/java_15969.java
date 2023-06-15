/* 15969
 * N명의 학생들의 점수가 주어졌을 때
 * 가장 높은 점수와 가장 낮은 점수의 차이 출력하기
 */

import java.util.*;
public class java_15969 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int students = scanner.nextInt();
        int max_score = Integer.MIN_VALUE;
        int min_score = Integer.MAX_VALUE;

        for(int i = 0; i < students; i++) {
            int current_score = scanner.nextInt();
            max_score = Math.max(current_score, max_score);
            min_score = Math.min(current_score, min_score);
        }
        
        System.out.println(max_score - min_score);
        scanner.close();
    }
}
