/* 30224
 * 1. 주어진 숫자에 7이 포함되지 않고 7로 나누어지지 않을 때: 0 출력
 * 2. 주어진 숫자에 7이 포함되지 않고 7로 나누어질 때: 1 출력
 * 3. 주어진 숫자에 7이 포함되고 7로 나누어지지 않을 때: 2 출력
 * 4. 주어진 숫자에 7이 포함되고 7로 나누어질 때: 3 출력
 */
 
import java.util.Scanner;
public class java_30224{
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String num = scanner.nextLine();
		boolean flag = false;
		
		for (int i = 0; i < num.length(); i++) {
		    if (num.charAt(i) == '7') {
		        flag = true;
		        break;
		    }
		}
		
		int num2 = Integer.valueOf(num);
		
		if (flag) {
		    if (num2 % 7 == 0) {
		        System.out.print(3);
		    }
		    else {
		        System.out.print(2);
		    }
		}
		else {
		    if (num2 % 7 == 0) {
		        System.out.print(1);
		    }
		    else {
		        System.out.print(0);
		    }
		}
		scanner.close();
	}
}
