/* 10103
 * 테스트 케이스만큼 주사위를 던져서 낮은 숫자가 나온 사람은
 * 상대편 주사위의 숫자만큼 점수를 잃게 됨
 * 같은 숫자면 아무도 점수를 잃지 않는다.
 */

import java.util.*;
public class java_10103 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();
        int my_score = 100;
        int your_score = 100;

        for (int i = 0; i < test; i++) {
            int me = scanner.nextInt();
            int you = scanner.nextInt();

            if (me > you) {
                your_score -= me;
            }

            else if (you > me) {
                my_score -= you;
            }

            else {
                continue;
            }
        }

        System.out.println(my_score);
        System.out.println(your_score);
        
        scanner.close();
    }
}
