/* 5054
 * 테스트 케이스만큼 방문할 상점의 개수와 상점의 위치가 주어진다.
 * 모든 상점을 방문하고 차로 돌아오기 위해 걸어야하는 거리의 최솟값 구하기
 * 길은 일직선이다.
 */

import java.util.*;
public class java_5054 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();

        for(int i = 0; i < test; i++) {
            int min_num = Integer.MAX_VALUE;
            int max_num = Integer.MIN_VALUE;

            int store_num = scanner.nextInt();

            for(int j = 0; j < store_num; j++) {
                int cur_store = scanner.nextInt();

                max_num = Math.max(cur_store, max_num);
                min_num = Math.min(cur_store, min_num);
            }
            
            System.out.println((max_num - min_num) * 2);
        }

        scanner.close();
    }
}
