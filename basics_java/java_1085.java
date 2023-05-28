/* 1085
 * x, y에 있을 때 직사각형의 경계선까지 가는 거리의 최솟값 구하기
 */

import java.util.*;
public class java_1085 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        // 현재 위치 좌표
        int x = scanner.nextInt();
        int y = scanner.nextInt();

        // 직사각형의 오른쪽 위 꼭짓점
        int w = scanner.nextInt();
        int h = scanner.nextInt();

        int half_x = w / 2;
        int half_y = h / 2;

        if (w % 2 != 0) half_x += 1;
        if (h % 2 != 0) half_y += 1;

        int result_x = 0;
        int result_y = 0;
        int result = 0;

        if((x >= half_x) && (y >= half_y)){
            result_x = w - x;
            result_y = h - y;

            result = Math.min(result_x, result_y);
        }

        else if((x < half_x) && (y >= half_y)){
            result_x = x;
            result_y = h - y;

            result = Math.min(result_x, result_y);
        }

        else if((x < half_x) && (y < half_y)) {
            result_x = x;
            result_y = y;

            result = Math.min(result_x, result_y);
        }

        else {
            result_x = w - x;
            result_y = y;

            result = Math.min(result_x, result_y);
        }

        System.out.println(result);
        

        scanner.close();
    }
}