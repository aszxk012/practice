/* 17608
 * 높이만 다른 같은 모양의 막대를 일렬로 세운 후 오른쪽에서 봤을 때
 * 보이는 막대의 수 구하기
 * 같은 높이의 막대가 있을 수 있다.
 */

import java.util.*;
public class java_17608 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int nums[] = new int[num];
        int result = 0;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < num; i++){
            nums[i] = scanner.nextInt();
        }

        for (int i = num - 1; i >= 0; i--) {
            if (max < nums[i]) {
                result += 1;
                max = nums[i];
            }
        }

        System.out.println(result);

        scanner.close();
    }
}
