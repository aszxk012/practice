/* 18017
 * 자신이 총과 함께 과녁을 향해 초속 A미터로 달리고 있을 때
 * 초속 B미터로 나가는 총알을 과녁 방향으로 발사했을 때, 총알의 과녁 속도 구하기
 * 오답 추후 수정(23.10.25)
 */

import java.util.Scanner;
public class java_18017 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        float a = scanner.nextFloat();
        float b = scanner.nextFloat();

        System.out.print((a + b) / (1 + a * b / (299792458 * 299792458)));
        scanner.close();
    }
}
