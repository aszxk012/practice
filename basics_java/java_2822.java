/* 2822
 * 8줄에 걸쳐서 문제에 대한 참가자의 점수가 주어진다.
 * 참가자의 총 점수는 가장 높은 점수 5개의 합이다.
 * 참가자의 총 점수와 어떤 문제가 최종 점수에 포함되는지 출력하기
 * 추후 수정(2023.07.09)
 */

import java.util.Scanner;
import java.util.ArrayList;
public class java_2822 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int scores[] = new int[8];
        ArrayList<Integer> max_scores = new ArrayList<Integer>();
        int sum = 0;

        for (int i = 0; i < 8; i++) {
            scores[i] = scanner.nextInt();
        }

        for (int score : scores) {
            if (max_scores.size() < 5) {
                max_scores.add(score);
                sum += score;
            }
            else {
                for (int i = 0; i < 5; i++) {
                    if (score > max_scores.get(i)) {
                        sum -= max_scores.get(i);
                        max_scores.remove(Integer.valueOf(max_scores.get(i)));
                        max_scores.add(score);
                        sum += score;
                    } 
                }
            }
        }

        System.out.println(sum);
        for (int score : max_scores) {
            System.out.print(score + " ");
        }
        scanner.close();
    }
}
