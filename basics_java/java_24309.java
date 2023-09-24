/* 24309
 * a * x = b - c를 만족하는 x 찾기
 */

import java.util.*;
import java.math.BigInteger;
public class java_24309 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        BigInteger a = scanner.nextBigInteger();
        BigInteger b = scanner.nextBigInteger();
        BigInteger c = scanner.nextBigInteger();

        System.out.println((b.subtract(c)).divide(a));
        scanner.close();
     }
 }
 