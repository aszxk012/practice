/* 1259
 * 입력한 수가 팰린드롬인지 판별하기
 */

import java.util.*;
public class java_1259 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String result = "";

        while (true) {
            String num = scanner.nextLine();
            if (num.equals("0")) {
                break;
            }

            boolean palindrome = true;
            int len = num.length();

            for (int i = 0; i < len / 2; i++){
                if (num.charAt(i) != num.charAt(len - i - 1)) {
                    palindrome = false;
                    break;
                }
            }

            if (palindrome) {
                result = "yes";
            }
            else {
                result = "no";
            }
            
            System.out.println(result);

        }
        
        scanner.close();
    }
}
