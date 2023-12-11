/* 30328
 * 등록비는 팀당 4000달러일 때, 얼마를 지원해야하는지 출력하기
 * 팀 수는 20이하의 정수가 입력된다.
 */

import java.util.Scanner;
public class java_30328{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int team = scanner.nextInt();
		System.out.println(team * 4000);
		
		scanner.close();
	}
}