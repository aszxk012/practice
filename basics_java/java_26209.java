/* 26209
 * 입력으로 주어지는 비트 목록을 성공적으로 읽었으면 S를
 * 그 중 9가 섞여 있어 읽지 못했다면 F를 출력하기
 */

import java.util.Scanner;
public class java_26209 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        boolean flag = false;

        for (int i = 0; i < 8; i++) {

            int n = scanner.nextInt();

            if (n == 9) {
                flag = true;
            }
        }

        if (flag) {
            System.out.print("F");
        }
        else {
            System.out.print("S");
        }
        
        scanner.close();
    }   
}
