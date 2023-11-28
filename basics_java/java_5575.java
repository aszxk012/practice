/* 5575
 * A, B, C의 출퇴근 시간을 입력할 때
 * A씨의 근무시간, B씨의 근무시간, C씨의 근무시간 출력하기
 * h 시간 m 분 s 초일 때 h m s 형식으로 출력
 */

import java.util.Scanner;
public class java_5575 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 3; i++){
            int company[] = new int[6];

            for (int j = 0; j < 6; j++) {
                company[j] = scanner.nextInt();
            }

            int s = company[5] - company[2];
            int m = company[4] - company[1];
            int h = company[3] - company[0];

            if (s < 0) {
                s += 60;
                m -= 1;
            }

            if (m < 0) {
                m += 60;
                h -= 1;
            }
            
            System.out.println(h + " " + m + " " + s);
        }
        scanner.close();
    }
}
