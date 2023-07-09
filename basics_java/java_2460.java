/* 2460
 * 기차는 역 번호 순서대로 운행
 * 출발역에서 내린 사람 수와 종착역에서 탄 사람 수는 0
 * 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우 X
 * 기차의 최대 정원은 10,000명, 정원을 초과하여 타는 경우 X
 * 기차에 사람이 가장 많을 때 출력하기
 */
 
import java.util.*;
public class java_2460 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int drops[] = new int[10];
		int rides[] = new int[10];
		int people = 0;
		int max = Integer.MIN_VALUE;
		
		for (int i = 0; i < 10; i++) {
		    drops[i] = scanner.nextInt();
		    rides[i] = scanner.nextInt();
		}
		
		for (int i = 0; i < 10; i++) {
		    people -= drops[i];
		    people += rides[i];
		    
		    if (people > max) {
		        max = people;
		    }
		}
		
		System.out.println(max);
		
		scanner.close();
	}
}
