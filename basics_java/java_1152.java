/* 1152
 * 문자열이 주어졌을 때, 문자열의 단어 개수 구하기
 */

import java.util.*;
public class java_1152 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String string = scanner.nextLine().trim();
        String result[] = string.split(" ");
        int count = 0;
        for (int i = 0; i < result.length; i++){
            if (string.isEmpty()){
                count = 0;
                break;
            }
            count += 1;
        }

        System.out.println(count);
        scanner.close();
    }
}
