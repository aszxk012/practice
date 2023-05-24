/* 24723
 * 블록의 높이가 주어질 때 블록의 윗면만 이용하여 내려오는 최단경로의 경우의 수 구하기
 * 시야에 보이지 않는 블록은 없음
 */

import java.util.*;
public class java_24723 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int height = scanner.nextInt();
        int result = 1;
        for (int i = 0; i < height; i++){
            result *= 2;
        }

        System.out.println(result);
        
        scanner.close();
    }
}
