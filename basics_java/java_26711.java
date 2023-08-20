/* 26711
 * 5000자리 이하의 수 입력 받아 두 수 더하기
 */

import java.math.BigInteger;
import java.util.*;
public class java_26711 {
    public static void main(String args[]){
        Scanner scanner = new Scanner(System.in);
        BigInteger a = scanner.nextBigInteger();
        BigInteger b = scanner.nextBigInteger();
    
        System.out.println(a.add(b));

        scanner.close();
    }
}
