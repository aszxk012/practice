/* 10870
 * n번째 피보나치 수 출력 */

import java.util.*;
public class java_10870 {
    public static int fibo(int n) {
        int result = 0;
        if (n == 0) {
            result = 0;
        }
        else if (n == 1) {
            result = 1;
        }
        else {
            result = fibo(n - 1) + fibo(n - 2);
        }

        return result;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        System.out.println(fibo(num));
        scanner.close();
    }
}
