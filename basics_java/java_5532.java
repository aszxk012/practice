/* 5532
 * 방학 L일, 국어 숙제 A 페이지, 수학 숙제 B 페이지, 하루에 풀 수 있는 국어 C 페이지, 수학 D 페이지가 주어질때,
 * 숙제를 하지 않고 놀 수 있는 최대 날의 수 출력하기
 */

import java.util.Scanner;
public class java_5532 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int va = scanner.nextInt();
        int ko = scanner.nextInt();
        int ma = scanner.nextInt();
        int max_ko = scanner.nextInt();
        int max_ma = scanner.nextInt();
        int do_ko = 0, do_ma = 0;

        if (ko % max_ko != 0) {
            do_ko = ko / max_ko + 1;
        }
        else {
            do_ko = ko / max_ko;
        }

        if (ma % max_ma != 0) {
            do_ma = ma / max_ma + 1;
        }
        else {
            do_ma = ma / max_ma;
        }

        if (do_ko < do_ma) {
            va -= do_ma;
        }
        else {
            va -= do_ko;
        }
        
        System.out.println(va);
        scanner.close();
    }
}