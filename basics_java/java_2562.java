/* 2562
 * 서로 다른 9개의 수를 입력받아 최댓값을 찾고
 * 그 최댓값이 몇번째 수인지 출력하기
 */

import java.util.*;
public class java_2562 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        List<Integer> num = new ArrayList<Integer>();

        int max_num = Integer.MIN_VALUE;
        int max_num_index = 0;

        for (int i = 0; i < 9; i++){
            int cur_num = scanner.nextInt();
            num.add(i, cur_num);
        }

        for (int j = 0; j < 9; j++){
            max_num = Math.max(max_num, num.get(j));
            
            if (max_num == num.get(j)){
                max_num_index = j;
            }
        }

        max_num_index += 1;

        System.out.println(max_num);
        System.out.println(max_num_index);

        scanner.close();
    }
}
