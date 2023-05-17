/* 11720
 * 숫자 개수 입력받은 후 숫자 N개가 공백없이 주어질 때, 이 숫자를 모두 합해서 출력하기
 */

import java.util.*;
public class java_11720 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        
        // nextLine은 개행 문자를 읽어들이기 때문에
        // 입력받은 숫자 개수만큼 공백이 생김 >> 범위를 벗어나는 오류 발생
        scanner.nextLine(); // 개행 문자 제거
        String numbers = scanner.nextLine();
        int result = 0;

        for (int i = 0; i < num; i++){
            // String에서 index 위치에 있는 문자 값을 반환하는 함수 = charAt
            // charAt(i) >> index의 "문자" >> int 변수로 선언 >> 아스키 코드 값
            // 아스키 코드를 숫자로 출력하려면 문자 '0'(아스키 코드 값 48)을 빼줘야함
            int n = numbers.charAt(i) - '0';

            result += n;
        }
        
        System.out.println(result);
        
        scanner.close();
    }
}
