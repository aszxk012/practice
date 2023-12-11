/* 23235
 * 세상에서 가장 빠른 정렬 알고리즘
 * 정렬해야하는 여러 개의 테스트 케이스를 입력받는다.
 * 마지막 테스트 케이스 뒤에는 하나의 0으로 구성된 한 줄이 들어옴.
 * 각 테스트 케이스에 대해 테스트 케이스 번호에 이어 Sorting... done!을 출력한다.
 */

import java.util.*;
public class java_23235 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int count = 1;
        while (true) {
            int n = scanner.nextInt();
            
            if (n == 0) {
                break;
            }
            
            int nums[] = new int[n];

            for (int i = 0; i < n; i++) {
                nums[i] = scanner.nextInt();
            }

            System.out.print("Case ");
            System.out.print(count);
            System.out.println(": Sorting... done!");
            count++;
        }
        scanner.close();
    }
}
