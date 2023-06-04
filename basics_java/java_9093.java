/* 9093
 * 문장을 입력했을 때 문장의 단어 뒤집어서 출력하기
 * 추후 수정(2023.05.26)
 * 수정 완료(2023.06.04)
 */

import java.util.*;
public class java_9093 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        scanner.nextLine(); // 개행 문자 소비

        StringBuilder result = new StringBuilder();

        for (int i = 0; i < num; i++) {
            String string = scanner.nextLine();
            String words[] = string.split(" ");

            for (int j = 0; j < words.length; j++) {
                for (int k = words[j].length() - 1; k >= 0; k--) {
                    result.append(words[j].charAt(k));
                }
                result.append(' ');
            }
            result.append('\n');
        }

        System.out.print(result);

        scanner.close();
    }
}