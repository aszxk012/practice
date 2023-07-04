/* 11557
 * 테스트 케이스만큼 학교 수와 이름, 소비한 술의 양 입력받아
 * 소비가 가장 많은 학교 출력
 */

import java.util.*;
public class java_11557 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();
        scanner.nextLine(); // 첫 번째 개행 문자 소비

        for(int i = 0; i < test; i++) {
            int school_num = scanner.nextInt();
            scanner.nextLine(); // 개행 문자 소비
            
            int max_ach = Integer.MIN_VALUE;
            String max_sch = "";

            for(int j = 0; j < school_num; j++) {
                String school = scanner.next();
                int ach = scanner.nextInt();
                scanner.nextLine(); // 개행 문자 소비

                if (max_ach < ach) {
                    max_ach = ach;
                    max_sch = school;
                }
            }

            System.out.println(max_sch);
        }
        scanner.close();
    }
}
