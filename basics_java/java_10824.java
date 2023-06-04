/* 10824
 * 네 자연수가 주어질 때, A와 B를 이어 붙인 수와 C와 D를 이어 붙인 수의 합 구하기
 */

import java.util.*;
public class java_10824 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String nums[] = new String[4];
        for (int i = 0; i < 4; i++){
            nums[i] = scanner.next();
        }

        String ab = nums[0] + nums[1];
        String cd = nums[2] + nums[3];

        long a_b = Long.parseLong(ab);
        long c_d = Long.parseLong(cd);

        System.out.println(a_b + c_d);
        
        scanner.close();
    }
}
