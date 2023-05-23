/* 2338
 * 최대 1,000자리까지 입력받을 수 있음
 * A + B, A - B, A * B 출력
 */

import java.math.BigInteger;
import java.util.*;
public class java_2338 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        BigInteger a = scanner.nextBigInteger();
        BigInteger b = scanner.nextBigInteger();
        
        System.out.println(a.add(b));
        System.out.println(a.subtract(b));
        System.out.println(a.multiply(b));
        scanner.close();
    }
}
