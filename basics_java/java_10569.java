/* 10569
 * 테스트 케이스만큼 꼭짓점 개수와 모서리 개수가 주어질 때, 면의 개수 출력하기
 */

import java.util.*;

public class java_10569 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();
        int result[] = new int[test];

        for (int i = 0; i < test; i++) {
            int v = scanner.nextInt();
            int e = scanner.nextInt();

            result[i] = -v + e + 2;
        }

        for (int i = 0; i < test; i++) {
            System.out.println(result[i]);
        }
        scanner.close();
    }
}
