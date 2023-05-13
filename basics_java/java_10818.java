/* 10818
 * N개의 정수가 주어질 때, 최소, 최대 값 구하기
 */

import java.util.*;

public class java_10818 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        Integer num_list[] = new Integer[num];

        int max_num = Integer.MIN_VALUE;
        int min_num = Integer.MAX_VALUE;

        for (int i = 0; i < num; i++){
            num_list[i] = Integer.valueOf(scanner.nextInt());
        }

        for (int j = 0; j < num; j++){
            max_num = Math.max(num_list[j], max_num);
            min_num = Math.min(num_list[j], min_num);
        }

        System.out.print(min_num);
        System.out.print(" ");
        System.out.print(max_num);
        scanner.close();
    }
}
