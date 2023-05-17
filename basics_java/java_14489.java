/* 14489
 * 첫째줄에 두 통장 잔고를, 두번째줄에 치킨 한마리 가격이 주어질 때
 * 치킨을 두마리 살 수 있으면 사고 난 후 두 통장 잔고의 합을
 * 살수 없으면 현재 두 통장의 합을 출력
 */

import java.util.*;
public class java_14489 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextLong(), b = scanner.nextLong();
        long chicken = scanner.nextLong();
        long result = 0;

        if ((a + b) >= chicken * 2){
            result = (a + b) - (chicken * 2);
        }
        else {
            result = a + b;
        }

        System.out.println(result);

        scanner.close();
    }
}
