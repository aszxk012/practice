/* 11948
 * 물리, 화학, 생물, 지구과학, 역사, 지리 총 6과목 시험, 시험의 만점은 100점
 * 물리, 화학, 생물, 지구과학 중 3과목, 역사, 지리 중 1과목 선택
 * 시험 점수 합이 가장 높도록 과목 선택할 때, 선택 과목의 시험 점수 합 구하기
 */

import java.util.*;
public class java_11948{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int score[] = new int[6];
        
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;
        
        int sum = 0;
        int count = 0;

        // phy, che, bio, earth, / history, geo
        for (int i = 0; i < 6; i++) {
            score[i] = scanner.nextInt();
        }

        for (int i = 0; i < 4; i++) {
            if (min1 > score[i]) {
                min1 = score[i];
            }
        }

        if (score[4] >= score[5]){
            min2 = score[5];
        }
        else {
            min2 = score[4];
        }

        for (int i = 0; i < 6; i++) {
            if (min1 == score[i] || min2 == score[i]) {
                continue;
            }
            else {
                sum += score[i];
                count += 1;
            }
        }
        
        if (count != 4) {
            sum += min1;
        }

        System.out.println(sum);

        scanner.close();
    }
}