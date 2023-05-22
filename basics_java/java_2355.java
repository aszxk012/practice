/* 2355
 * A와 B가 주어졌을 때 사이에 있는 수의 합 구하기
 */

import java.util.*;
public class java_2355 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextLong();
        long b = scanner.nextLong();
        long result = 0;

        if (b >= a){
            result = ((a + b) * ((b - a) + 1) / 2);
        }
        else {
            result = ((b + a) * ((a - b) + 1) / 2);
        }
        System.out.println(result);

        scanner.close();
    }
}
