/* 15792
 * A/B 출력하기
 */

import java.util.*;
public class java_15792 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        System.out.print(a / b + ".");

        for(int i = 0; i < 2000; i++){
            a %= b;
            a *= 10;

            System.out.print(a / b);
        }
        
        scanner.close();
    }
}
