/* 27389
 * 메트로놈 키가 완전히 회전할 때마다 4틱을 줄 때, 노래의 끝에서 메트로놈이 멈추길 원한다.
 * 메트로놈 키를 몇 바퀴 감아햐 하는지 소수점 두번째 자리까지 출력하기
 */

import java.util.*;
public class java_27389 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        float key = (float)n / 4;

        System.out.printf("%.2f", key);
        scanner.close();
    }
}
