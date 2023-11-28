/* 16600
 * 이미지 넓이가 주어질 때 해당 이미지의 둘레 출력하기
 */

import java.util.Scanner;
public class java_16600 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        long a = scanner.nextLong();
        double cm = Math.sqrt(a);
        double circum = cm * 4;

        System.out.printf("%.8f", circum);
        scanner.close();
    }
}
