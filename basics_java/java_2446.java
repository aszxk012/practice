/* 2446
 * 별 찍기 9
 */

import java.util.*;

public class java_2446 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();
        String star = "*";
        String space = " ";
        String result = "";
        for (int i = num; i > 0; i--){
            result = space.repeat(num - i) + star.repeat((i * 2) - 1);
            System.out.println(result);
        }

        for (int j = 2; j <= num; j++){
            result = space.repeat(num - j) + star.repeat((j * 2) - 1);
            System.out.println(result);
        }

        scanner.close();
    }
}
