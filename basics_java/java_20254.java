/* 20254
 * 2020 타이페이-신주 지역 대회의 지역 배정 점수를 구하는 프로그램
 * UR = 지역 대회에서 최소 한 문제를 푼 대학의 수
 * TR = 지역 대회에서 최소 한 문제를 푼 팀의 수
 * UO = TOPC에서 최소 한 문제를 푼 대학의 수
 * TO = TOPC에서 최소 한 문제를 푼 팀의 수
 * 지역 배정 점수 = 56UR + 24TR + 14UO + 6TO
 */

import java.util.Scanner;
public class java_20254 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int ur = scanner.nextInt();
        int tr = scanner.nextInt();
        int uo = scanner.nextInt();
        int to = scanner.nextInt();

        int result = (56 * ur) + (24 * tr) + (14 * uo) + (6 * to);
        
        System.out.println(result);
        scanner.close();
    }
}
