/* 8760
 * w 개의 열과 k 개의 행을 이루는 w * k 크기의 직사각형 공간
 * 여행객은 인접한 두 구역을 차지함. -> 눕힌다고 이해하면 쉬움
 * 한 구역을 최대 한 명의 여행객에게 배정한다고 할 때
 * 최대 몇 명의 여행객을 배정할 수 있는지 출력하기
 */

import java.util.Scanner;
public class java_8760 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();

        for (int i = 0; i < test; i++) {
            int w = scanner.nextInt();
            int h = scanner.nextInt();
            int space = w * h;

            int people = space / 2;

            System.out.println(people);
        }
        scanner.close();
    }
}
