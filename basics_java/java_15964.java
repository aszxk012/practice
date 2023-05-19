/* 15964
 * A＠B = (A+B)×(A-B)
 */

import java.util.*;
public class java_15964 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextLong(), b = scanner.nextLong();
        long result = 0;

        result = (a + b) * (a - b);

        System.out.println(result);

        scanner.close();
    }
}
