/* 2587
 * 한 줄에 하나씩 5개의 자연수가 주어진다.
 * 첫째 줄엔 평균을, 둘째 줄엔 중앙값 출력하기
 */

import java.util.*;
public class java_2587 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int avg = 0;
        int mid = (5 / 2);
        int nums[] = new int[5];
        
        for (int i = 0; i < 5; i++) {
            nums[i] = scanner.nextInt();
            avg += nums[i];
        }
        
       Arrays.sort(nums);
        avg = avg / 5;
        mid = nums[mid];

        System.out.println(avg);
        System.out.println(mid);
        scanner.close();
    }
}
