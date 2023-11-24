/* 16099
 * 어느 학교가 더 넓은지 출력하기, 넓이가 같다면 Tie 출력
 * lt, wt는 TelecomParisTech, le, we는 Eurocom의 길이가 주어진다.
 */

import java.util.Scanner;
public class java_16099 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        for (int i = 0; i < n; i++) {
            long lt = scanner.nextLong();
            long wt = scanner.nextLong();
            long le = scanner.nextLong();
            long we = scanner.nextLong();

            long t = lt * wt;
            long e = le * we;

            if (t < e) {
                System.out.println("Eurecom");
            }
            else if (e < t) {
                System.out.println("TelecomParisTech");
            }
            else {
                System.out.println("Tie");
            }
        }
        scanner.close();
    }
}
