/* 5522
 * 총 5회 진행되는 카드 게임의 득점이 주어질 때, 총점 구하기
 */

import java.util.*;
public class java_5522 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        for (int i = 0; i < 5; i++) {
            int score = scanner.nextInt();

            sum += score;
        }

        System.out.println(sum);
        scanner.close();
    }
}
