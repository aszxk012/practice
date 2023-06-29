/* 8370
 * 비즈니스 석 n1개의 열, 이코노미 석 n2개의 열
 * 비즈니스 석의 각 열에는 k1개의 좌석, 이코노미 석의 각 열에는 k2개의 좌석
 * 비행기의 총 좌석의 개수 출력
 * n1, k1, n2, k2 순으로 입력
 */

import java.util.*;
public class java_8370 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n1 = scanner.nextInt();
        int k1 = scanner.nextInt();
        int n2 = scanner.nextInt();
        int k2 = scanner.nextInt();
        int seats = (n1 * k1) + (n2 * k2);

        System.out.println(seats);
        
        scanner.close();
    }
}
