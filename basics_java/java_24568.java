/* 24568
 * 큰 컵케이크 박스에는 8개의 컵케이크가, 작은 컵케이크 박스에는 3개의 컵 케이크가 들어간다.
 * 총 28명의 학생들이 컵케이크를 한 개씩 가져가고 난 후
 * 컵케이크가 몇 개 남았는지 출력하기
 */

import java.util.Scanner;
public class java_24568 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int big = scanner.nextInt();
        int small = scanner.nextInt();

        int big_cup = big * 8;
        int small_cup = small * 3;

        System.out.println(big_cup + small_cup - 28);
        
        scanner.close();
    }
}
