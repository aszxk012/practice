/* 11023
 * 수 N개가 주어졌을 때 합 구하기
 */

import java.util.*;
public class java_11023 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        List<Integer> number_list = new ArrayList<Integer>();
        int count = 0;
        int result = 0;
        while (scanner.hasNextInt()){
            int num = scanner.nextInt();
            number_list.add(count, num);
            count += 1;
        }

        for (int i = 0; i < count; i++){
            result += number_list.get(i);
        }
        
        System.out.println(result);
        
        scanner.close();
    }
}
