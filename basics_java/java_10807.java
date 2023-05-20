/* 10807
 * N개만큼 숫자를 입력 받은 후 세 번째 수의 개수 출력하기
 */
import java.util.*;
public class java_10807 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int num_array[] = new int[num];

        for (int i = 0; i < num; i++){
            num_array[i] = scanner.nextInt();
        }

        int find_num = scanner.nextInt();
        int count = 0;

        for (int j = 0; j < num; j++){
            if (num_array[j] == find_num) {
                count += 1;
            }
        }

        System.out.println(count);
        scanner.close();
    }
}
