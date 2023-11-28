/* 30676
 * 파장을 입력받아 별의 색 출력하기
 * 620 ~ 780: 빨간색, 590 ~ 620: 주황색, 570 ~ 590: 노란색
 * 495 ~ 570: 초록색, 450 ~ 495: 파란색, 425 ~ 450: 남색
 * 380 ~ 425: 보라색
 */

import java.util.Scanner;
public class java_30676 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int nm = scanner.nextInt();

        if ((nm >= 620) & (nm <= 780)){
            System.out.println("Red");
        }
        else if ((nm >= 590) & (nm < 620)) {
            System.out.println("Orange");
        }
        else if ((nm >= 570) & (nm < 590)) {
            System.out.println("Yellow");
        }
        else if ((nm >= 495) & (nm < 570)) {
            System.out.println("Green");
        }
        else if ((nm >= 450) & (nm < 495)) {
            System.out.println("Blue");
        }
        else if ((nm >= 425) & (nm < 450)) {
            System.out.println("Indigo");
        }
        else {
            System.out.println("Violet");
        }
        
        scanner.close();
    }
}
