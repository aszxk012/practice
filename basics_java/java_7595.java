/* 7595
 * 1 <= n <= 100인 n이 입력될 때 그 수 크기의 삼각형 그리기
 * 0이 입력되면 종료
 */

import java.util.Scanner;
public class java_7595 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int n = scanner.nextInt();

            if (n == 0) {
                break;
            }

            else {
                String string = "";

                for (int i = 1; i <= n; i++) {
                    string += "*";
                    System.out.println(string);
                }
            }
        }
        scanner.close();
    }
}
