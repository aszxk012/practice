/* 2845
 * 1m^2 당 사람수와 파티가 열렸던 곳의 넓이를 입력받아
 * 기사에 실린 참가자 수의 차이 출력하기
 */

import java.util.Scanner;
public class java_2845 {
	public static void main(String[] args) {
	    Scanner scanner = new Scanner(System.in);
		int people = scanner.nextInt();
		int meter = scanner.nextInt();
		int total = people * meter;
		
		for (int i = 0; i < 5; i++) {
		    int news = scanner.nextInt();
		    System.out.print(news - total + " ");
		}
	}
}