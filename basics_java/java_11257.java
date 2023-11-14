/* 11257
 * 전략 35, 경영 25, 기술 40, 총점 55 이상, 각 분야마다 30% 이상
 * 응시자 수와 응시번호, 점수가 공백으로 구분되어 입력됨
 * 응시번호, 점수, FAIL/PASS 출력하기
 */

import java.util.Scanner;
public class java_11257 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        int num = scanner.nextInt();
        double sta_30 = 35 * 0.3;
        double it_30 = 25 * 0.3;
        double tech_30 = 40 * 0.3;

        for (int i = 0; i < num; i++) {
            int stu_id = scanner.nextInt();

            int sta = scanner.nextInt();
            int it = scanner.nextInt();
            int tech = scanner.nextInt();

            int sum = 0;

            sum = sta + it + tech;

            if ((sum >= 55) & (sta >= sta_30) & (it >= it_30) & (tech >= tech_30)) {
                System.out.println(stu_id + " " + sum + " PASS");
            }
            else {
                System.out.println(stu_id + " " + sum + " FAIL");
            }
            
        }
        scanner.close();
    }
}
