/* 10871
 * N개의 정수로 이루어진 수열과 정수 x가 주어졌을때
 * 수열에서 x보다 작은 수를 모두 출력하기
 */


import java.util.*;
public class java_10871 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        
        int list_len = scanner.nextInt();
        Integer num_list[] = new Integer[list_len];
        List<Integer> result = new ArrayList<Integer>();
        
        int num = scanner.nextInt();

        for (int i = 0; i < list_len; i++){
            num_list[i] = scanner.nextInt();
        }

        for (int j = 0; j < list_len; j++){
            if (num > num_list[j]){
                result.add(num_list[j]);
            }
        }

        for (int k = 0; k < result.size(); k++){
            System.out.print(result.get(k));
            if (k + 1 >= result.size()) {
                break;
            }
            System.out.print(" ");
        }
        scanner.close();
    }
}