/* 11549
 * 홍차 종류를 의미하는 숫자(1 ~ 4)가 주어지고 A, B, C, D, E가
 * 어떤 종류의 홍차인지 답한다.
 * 이때 몇 명이 맞췄는지 출력하기
 */

import java.util.*;
public class java_11549 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int tea = scanner.nextInt();
        String ans[] = new String[5];
        int count = 0;

        for (int i = 0; i < ans.length; i++) {
            ans[i] = scanner.next();
        }

        for (int j = 0; j < ans.length; j++) {
            if (ans[j].equals(String.valueOf(tea))) {  
                count += 1;
            }
        }
        
        System.out.println(count);

        scanner.close();
    }
}
