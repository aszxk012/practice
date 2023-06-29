/* 16486
 * 운동장의 둘레 구하기
 */

import java.util.*;
public class java_16486 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        double d1 = scanner.nextDouble(); // 직사각형의 가로
        double d2 = scanner.nextDouble(); // 반원의 반지름
        double pi = 3.141592;

        double len = (d2 * 2 * pi) + (d1 * 2);
        System.out.println(len);
        scanner.close();
    }
}
