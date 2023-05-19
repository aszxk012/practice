/* 10872
 * N! 출력하기
 */

import java.util.*;
public class java_10872 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        long result = 1;

        if (num == 0) {
            result = 1;
        }

        else {
            for (int i = num; i > 0; i--){
                result *= i;
            }
        }
        System.out.println(result);
        scanner.close();
    }
}
