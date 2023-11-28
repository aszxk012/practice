/* 6887
 * 한 변이 1cm인 정사각형 타일을 n개 입력받아
 * 만들 수 있는 가장 큰 정사각형의 한 변의 길이 출력하기
 */

import java.util.Scanner;
public class java_6887 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int side = (int) Math.sqrt((double) n);
        System.out.println("The largest square has side length " + side + ".");
        scanner.close();
    }
}
