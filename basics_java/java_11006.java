/* 11006
 * 테스트 케이스만큼 닭의 다리 수와 닭의 수가 주어진다.
 * 닭의 다리는 하나씩만 사라진다.
 * 다리가 잘린 닭의 수와 멀쩡한 닭의 수 출력하기
 * 추후 수정 (2023.07.06)
 */

import java.util.*;
public class java_11006 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int num = scanner.nextInt();
		int legs = 0;
		int chicken = 0;
		
		for (int i = 0; i < num; i++) {
		    int n = scanner.nextInt();
		    int m = scanner.nextInt();
		    
		    if ((m * 2) > n) {
		        legs = (m * 2) - n;
		        chicken = m - legs;
		    }
		    
		    System.out.println(legs + " " + chicken);
		}
		scanner.close();
	}
}
/*
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		for (int i = 0; i < N; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			System.out.println((b * 2 - a) + " " + (b - (b * 2 - a)));
		}
		sc.close();
	}
}*/