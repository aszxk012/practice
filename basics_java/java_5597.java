/* 5597
 * 30명 중 2명이 과제를 제출하지 않았는데 과제를 제출하지 않은 2명의
 * 출석 번호 구하기
 * 첫 번째 줄에 두 수 중 작은 수, 두 번째 줄에 두 수 중 큰 수 출력
 */

import java.util.*;
public class java_5597 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int input_student_num[] = new int[28];
        List<Integer> result = new ArrayList<Integer>();

        for (int i = 0; i < 28; i++){
            int num = scanner.nextInt();
            input_student_num[i] = num;
        }

        for (int j = 1; j < 31; j++){
            boolean flag = false;
           for (int number : input_student_num){
                if (number == j) {
                    flag = true;
                    break;
                }
           }
           
           if (!flag) {
            result.add(j);
           }
        }

       int small = Math.min(result.get(0), result.get(1));
       int big = Math.max(result.get(0), result.get(1));

       System.out.println(small);
       System.out.println(big);
        
        scanner.close();
    }
}
