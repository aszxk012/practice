/* 3003
 * 체스 말은 킹, 퀸, 룩, 비숍, 나이트, 폰으로 구성되어 있다.
 * 1, 1, 2, 2, 2, 8개로 구성되어 있을 때 입력 받은 체스 세트는
 * 몇 개의 말을 더하고 빼야 올바른 세트가 되는지 출력하기
 */

import java.util.Scanner;
public class java_3003 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int chess[] = {1, 1, 2, 2, 2, 8};
        int result[] = new int[6];

        for (int i = 0; i < 6; i++) {
            int n = scanner.nextInt();
            result[i] = chess[i] - n;
            System.out.print(result[i] + " ");
        }
        scanner.close();
    }
}
