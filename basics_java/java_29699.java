/* 29699
 * "WelcomeToSMUPC"가 반복적으로 적혀있다.
 * N번째 글자가 있는 곳까지 라벨지를 자를 때, N번째에 어떤 글자가 있을 지 출력하기
 */

import java.util.Scanner;
public class java_29699{
   public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str = "WelcomeToSMUPC";
        int len = str.length();
        int n = scanner.nextInt();

        if (n <= len) {
            n -= 1;
        }
        else if (n > len) {
            n = (n - 1) % len;
        }

        System.out.println(str.charAt(n));
        scanner.close();
   }
}