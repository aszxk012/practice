/* 4344
 * 테스트 개수가 주어지고 각 테스트 케이스의 학생 수와 점수가 주어진다.
 * 각 줄의 평균을 넘는 학생의 비율을 반올림하여 소수점 셋째자리까지 표현
 */

import java.util.*;
public class java_4344 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();

        for(int i = 0; i < num; i++) {
            int students = scanner.nextInt();
            int scores[] = new int[students];
            double avg = 0;

            for(int j = 0; j < students; j++) {
                scores[j] = scanner.nextInt();
                avg += scores[j];
            }

            avg = (double) avg / students;
            double count = 0;
            double percent = 0;
            
            for(int score : scores) {
                if (score > avg) {
                    count += 1;
                }
            }
            
            percent = ((double) count / students) * 100;
            System.out.printf("%.3f%%\n", percent);
        }


        
        scanner.close();
    }
}
