/* 13623
 * 세 사람이 0, 1 중 하나의 값을 낸다.
 * 두 사람과 다른 값을 낸 사람 출력하기
 * 모두 다 같은 값을 냈다면 * 출력
 */

import java.util.Scanner;
public class java_13623 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();

        if ((a == b) && (b == c)) {
            System.out.println("*");
        }
        else if ((a == b) && (b != c)) {
            System.out.println("C");
        }
        else if ((a == c) && (b != c)) {
            System.out.println("B");
        }
        else if ((b == c) && (a != b)) {
            System.out.println("A");
        }
        scanner.close();
    }
}
