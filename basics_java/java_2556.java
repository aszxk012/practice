/* 2556
 * *로 꽉찬 사각형 출력하기
 */

import java.util.*;
public class java_2556 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        int num = scanner.nextInt();

        for (int i = 0; i < num; i++) {
            for(int j = 0; j < num; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        
        scanner.close();
    }
}
