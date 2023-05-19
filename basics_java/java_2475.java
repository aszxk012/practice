/* 2475
 * 고유번호 5자리의 각 숫자를 제곱한 수의 합을 10으로 나눈 나머지 = 검증수
 */

import java.util.*;
public class java_2475 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        Integer num[] = new Integer[5];
        int sum = 0;

        for (int i = 0; i < 5; i++){
            num[i] = scanner.nextInt();
            num[i] = num[i] * num[i];

            sum += num[i];
        }

        int result = sum % 10;

        System.out.println(result);
        scanner.close();
    }
}
