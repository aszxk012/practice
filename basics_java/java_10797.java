/* 10797
 * 10부제를 진행할 때, 일의 자리 숫자가 주어지고
 * 5대의 자동차의 일의 자리 숫자를 보고 10부제를 위반하는 차량의 수를 출력한다
 */

import java.util.Scanner;
public class java_10797 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int count = 0;

        for (int i = 0; i < 5; i++) {
            int cur = scanner.nextInt();
            if (cur == num) {
                count++;
            }  
        }

        System.out.println(count);
        
        scanner.close();
    }
}