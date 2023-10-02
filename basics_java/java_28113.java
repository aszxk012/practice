/* 28113
 * a분 뒤 정류소에 버스 도착, b분 뒤에 지하철 도착
 * 정류소에서 지하철 역까지 n분
 * 버스가 빠른지 지하철이 빠른지 출력하기
 * 도착하는 시간이 같다면 anything 출력하기
 */

import java.util.*;
public class java_28113{
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        int bus = a;
        int subway = b;

        if (bus > subway) {
            System.out.println("Subway");
        }

        else if (bus < subway) {
            System.out.println("Bus");
        }

        else {
            System.out.println("Anything");
        }
        scanner.close();
    }
}