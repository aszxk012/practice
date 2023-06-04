/* 1284
 * 주소 호수판 길이 구하기
 * 1 = 2cm, 2 = 3cm, 0 = 4cm
 * 숫자와 숫자 사이에 공백 1cm
*/

import java.util.*;
public class java_1284 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        List<Integer> result = new ArrayList<Integer>();
        
        while(true){
            int size = 0;
            String num = scanner.nextLine();
            if (num.equals("0")){
                break;
            }

            char digits[] = num.toCharArray();
            for (char digit : digits){
                size += 1;

                if (digit == '1'){
                    size += 2;
                }
                else if (digit == '0'){
                    size += 4;
                }
                else {
                    size += 3;
                }
            }
            size += 1; // 마지막 숫자 뒤에 공백
            result.add(size);
        }

        for(int i : result){
            System.out.println(i);
        }
        
        scanner.close();
    }
}
