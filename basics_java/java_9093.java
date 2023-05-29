/* 9093
 * 문장을 입력했을 때 문장의 단어 뒤집어서 출력하기
 * 추후 수정(2023.05.26)
 */

import java.util.*;
public class java_9093 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int count = 0;

        while (true){
            String string = scanner.nextLine();
            String[] words = string.split(" ");

            for (int i = 0; i < words.length; i++) {
                for (int j = words[i].length() - 1; i >= 0; i--){
                    System.out.print(string.charAt(j));
                }
            }

            count++;
            if (count == num) break;

        }

        scanner.close();
    }
}
