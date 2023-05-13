/* 11654
 * 알파벳 대문자, 소문자, 0-9까지 주어졌을 때
 * 주어진 글자를 아스키코드값으로 출력하기
 */

import java.util.*;

public class java_11654 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        // String이 아닌 char 타입으로 입력 받기
        // char 타입이 아스키 코드 규칙에 맞게 환되어 저장되기 때문
        // -> int타입으로 바꿔주는 것은 문자열로 출력되기 떄문
        char s = scanner.nextLine().charAt(0);
        int num = (int)s;
        System.out.println(num);

        scanner.close();
    }
}