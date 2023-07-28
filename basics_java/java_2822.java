/* 2822
 * 8줄에 걸쳐서 문제에 대한 참가자의 점수가 주어진다.
 * 참가자의 총 점수는 가장 높은 점수 5개의 합이다.
 * 참가자의 총 점수와 어떤 문제가 최종 점수에 포함되는지 출력하기
 * 추후 수정(2023.07.09) > index 출력 추후 수정(2023.07.16) > 수정(2023.07.28)
 */

import java.util.*;

public class java_2822 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int scores[] = new int[8];
        int index[] = new int[8];
        int sum = 0;

        for (int i = 0; i < 8; i++) {
            scores[i] = scanner.nextInt();
            index[i] = i + 1;
        }

        // 배열을 내림차순으로 정렬하기 위해 별도의 Comparator를 사용
        Integer[] indexWrapper = new Integer[8];
        for (int i = 0; i < 8; i++) {
            indexWrapper[i] = i;
        }
        Arrays.sort(indexWrapper, (a, b) -> scores[b] - scores[a]);

        for (int i = 0; i < 5; i++) {
            sum += scores[indexWrapper[i]];
        }

        System.out.println(sum);

        // 인덱스를 오름차순으로 정렬하여 출력
        Arrays.sort(indexWrapper, 0, 5);
        for (int i = 0; i < 5; i++) {
            System.out.print((indexWrapper[i] + 1) + " ");
        }

        scanner.close();
    }
}