/* 13277
 * 큰 수 A, B 곱하여 출력하기
 */

import java.math.BigInteger;
import java.util.*;
public class java_13277 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        BigInteger a = scanner.nextBigInteger();
        BigInteger b = scanner.nextBigInteger();

        System.out.println(a.multiply(b));
        scanner.close();
    }
}
