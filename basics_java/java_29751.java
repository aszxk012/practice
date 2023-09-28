/* 29751
 * 밑변 w, 높이 h인 삼각형의 넓이 구하기
 */

import java.util.*;
public class java_29751 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        float w = scanner.nextFloat();
        float h = scanner.nextFloat();

        float result = (w * h) / 2;
        System.out.printf("%.1f", result);
        scanner.close();
    }
}
