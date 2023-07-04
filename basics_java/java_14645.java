/* 14645
 * 첫 출발역과 종착역을 제외한 정거장의 수와 출발역에서 탑승하는 사람의 수가 주어짐.
 * 둘째 줄부터 N개의 줄에 걸쳐 줄마다 탑승하는 인원과 하차하는 인원이 주어짐.
 * 종착역에 도착했을 때, 버스 운전수의 이름 출력하기
 */

import java.util.*;
public class java_14645 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int people = scanner.nextInt();

        for (int i = 0; i < num; i++) {
            int ride = scanner.nextInt();
            int drop = scanner.nextInt();

            people += ride;
            people -= drop;
        }

        System.out.println("비와이");
        scanner.close();
    }
}
