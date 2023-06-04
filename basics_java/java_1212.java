/* 1212
 * 8진수가 주어졌을 때, 2진수로 변환하여 출력하기
 */

import java.util.*;
public class java_1212 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        String octal_string = scanner.nextLine();
        int octal_length = octal_string.length();
        StringBuilder result_builder = new StringBuilder(octal_length * 3);

        for (int i = 0; i < octal_length; i++){
            char octal_num = octal_string.charAt(i);
            int octal_digit = Character.getNumericValue(octal_num);
            String binary = Integer.toBinaryString(octal_digit);

            if (i != 0){
                while (binary.length() < 3) {
                binary = "0" + binary;
                }
            }

            result_builder.append(binary);
        }
        String result = result_builder.toString();
        System.out.println(result);
        scanner.close();
    }
}
