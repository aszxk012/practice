/* 11721
 * 10글자씩 끊어서 출력하기
 */

import java.util.*;

public class java_11721 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String str = scanner.next();

        for (int i = 0; i < str.length(); i++) {
            if (i != 0) {
                if (i % 10 == 0) {
                    System.out.println();
                }
            }
            
            System.out.print(str.charAt(i));

        }

        scanner.close();
    }
}
