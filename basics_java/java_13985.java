/* 13985
 * a + b = c 형태의 입력이 들어올 때 해당 수식이 참이면 YES를, 거짓이면 NO 출력
 * 어디에서 문제 된건지 모르겠음 >> 추후 수정(2023.11.07), 계속 에러 발생(2023.12.01)
 * python으로 해결
 */

import java.util.Scanner;
public class java_13985 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        String equality = scanner.nextLine();

        int a = Character.getNumericValue(input.charAt(0));
        int b = Character.getNumericValue(input.charAt(4));
        int c = Character.getNumericValue(input.charAt(8));

        int sum = a + b;

        if (sum == c) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

        scanner.close();
    }
}
