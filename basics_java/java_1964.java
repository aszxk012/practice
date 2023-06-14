/* 1964
 * 오각형의 점의 개수가 규칙적으로 증가한다.
 * N단계에서 점의 개수를 구한 후 45678로 나눈 나머지 출력
 */

import java.util.*;
public class java_1964 {
    public static long pentagon(long num) {
        long point = 5;
        long point_plus = 7;
        for (long i = 1; i < num; i++) {
            point += point_plus;
            point_plus += 3;
        }

        return point;
    }
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        long num = scanner.nextLong();
        long point = pentagon(num);

        System.out.println(point % 45678);
        scanner.close();
    }
}
