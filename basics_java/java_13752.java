/* 13752
 * 테스트 케이스만큼 데이터 히스토그램으로 시각화하기
 */

import java.util.*;
public class java_13752 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int test = scanner.nextInt();
		int data[] = new int[test];
		
		for (int i = 0; i < test; i++) {
		    data[i] = scanner.nextInt();
		}
		
		for (int i = 0; i < test; i++) {
		    for (int j = 0; j < data[i]; j++){
		        System.out.print("=");
		    }
		    System.out.println();
		}
		scanner.close();
	}
}
