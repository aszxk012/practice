/* 4153
 * 주어진 세 변의 길이로 직각삼각형인지 아닌지 구분하기
 */

import java.util.*;
public class java_4153 {
    public static boolean isTriangle(int a, int b, int c){
        int max_num = Math.max(a, b);
        max_num = Math.max(max_num, c);
             
        if (max_num == a) {
            return (b * b) + (c * c) == (a * a);
        }
        else if (max_num == b){
            return (a * a) + (c * c) == (b * b);
        }
        else {
            return (a * a) + (b * b) == (c * c);
        }
    }
    
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        List<String> result = new ArrayList<String>();

        while(true){
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();

            if ((a == 0) && (b == 0) && (c == 0)) break;

            if (isTriangle(a, b, c) == true){
                result.add("right");
            }
            else {
                result.add("wrong");
            }
            
        }

        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
        scanner.close();
    }
}

