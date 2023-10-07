/* 28938
 * n개의 1, 0, -1 입력 받아 컨베이어가 어디로 이동하는지 출력하기
 * -1은 왼쪽, 1은 오른쪽, 0은 변화가 없었다.
 */

import java.util.Scanner;
public class java_28938 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int direction = 0;

        for (int i = 0; i < n; i++) {
            int x = scanner.nextInt();
            direction += x;
        }

        if (direction > 0) System.out.print("Right");
        else if (direction < 0) System.out.print("Left");
        else System.out.print("Stay");
        scanner.close();
    }
}
