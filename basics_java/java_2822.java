/* 2822
 * 8줄에 걸쳐서 문제에 대한 참가자의 점수가 주어진다.
 * 참가자의 총 점수는 가장 높은 점수 5개의 합이다.
 * 참가자의 총 점수와 어떤 문제가 최종 점수에 포함되는지 출력하기
 * 추후 수정(2023.07.09) > index 출력 추후 수정(2023.07.16)
 */

import java.util.*;
public class java_2822 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int scores[] = new int[8];
        int index[] = new int[8];
        int max_scores[] = new int[5];
        int sum = 0;

        for (int i = 0; i < 8; i++) {
            scores[i] = scanner.nextInt();
            index[i] = i + 1;
        }

        Arrays.sort(scores);
        
        for (int i = 0; i < 5; i++) {
            max_scores[i] = scores[7 - i];
            sum += max_scores[i];
        }

        System.out.println(sum);
        for (int i = 0; i < 5; i++) {
            System.out.print(index[i] + " ");
        }
        scanner.close();
    }
}
