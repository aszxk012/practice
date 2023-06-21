/* 15439
 * 상의 N벌과 하의 N벌이 있고, i번째의 상의와 i번째 하의는 같은 색이며,
 * 상의와 하의모두 다른 색의 옷이다.
 * 상의와 하의가 서로 다른 색상인 조합이 몇가지인지 출력하기
 */

import java.util.*;
public class java_15439 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        System.out.println(num * (num - 1));
        scanner.close();
    }
}
