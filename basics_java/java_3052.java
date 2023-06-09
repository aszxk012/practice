/* 3052
 * 수 10개를 입력받은 후, 42로 나눈 나머지를 구한다.
 * 이 나머지 중 서로 다른 값이 몇 개 있는지 출력하기
 */

import java.util.*;
public class java_3052 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int nums[] = new int[10];
        int rests[] = new int[10];
        int result[] = new int[10];
        int count = 10;

        for (int i = 0; i < 10; i++){
            nums[i] = scanner.nextInt();
            rests[i] = nums[i] % 42;
            result[i] = rests[i];
        }

        for (int j = 0; j < 10; j++){
            for (int k = 0; k < j; k++){
                if (rests[j] == result[k]) {
                    count--;
                    break;
                }
            }
        }

        System.out.println(count);
        scanner.close();
    }
}
