/* 30214
 * S1, S2를 입력받았을 때, S1이 S2의 절반 이상일 경우 E,
 * 그렇지 않을 경우 H 출력
 */

import java.util.Scanner;
public class java_30214 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int S1 = scanner.nextInt();
        int S2 = scanner.nextInt();
        float half = (float) S2 / 2;

        if (S1 >= half) {
            System.out.print("E");
        }
        else {
            System.out.print("H");
        }
        
        scanner.close();
    }
}