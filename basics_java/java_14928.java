/* 14928
 * 100만자리의 수 N이 주어질 때 20000303으로 나눈 나머지 출력하기
 */

import java.util.*;
public class java_14928 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();

        int modulo = 20000303;
        int remainder = 0;

        for (int i = 0; i < input.length(); i++) {
            int digit = Character.getNumericValue(input.charAt(i));
            remainder = (remainder * 10 + digit) % modulo;
        }

        System.out.println(remainder);
        scanner.close();
    }
}
