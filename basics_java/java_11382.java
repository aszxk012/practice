/* 11382
 * A + B + C 계산하기
 */

import java.util.*;
public class java_11382 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        long a = scanner.nextLong();
        long b = scanner.nextLong();
        long c = scanner.nextLong();

        System.out.println(a + b + c);

        scanner.close();
    }
}