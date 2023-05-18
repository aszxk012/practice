/* 2750
 * 첫째 줄에 수의 개수
 * 둘째 줄부터 숫자가 주어짐 > 오름차순으로 정렬
 */

import java.util.*;
public class java_2750 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        Integer number_list[] = new Integer[num];

        for(int i = 0; i < num; i++){
            number_list[i] = scanner.nextInt();
        }

        Arrays.sort(number_list);

        for(int j = 0; j < num; j++){
            System.out.println(number_list[j]);
        }
        
        scanner.close();
    }
}
