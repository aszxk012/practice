/* 10178
 * 테스트 케이스만큼 입력받기
 * 사탕의 개수와 형제의 수를 입력받아 내가 받는 사탕의 수와 남는 사탕의 수 출력하기
 */

import java.util.*;
public class java_10178 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();
        List<Integer> result = new ArrayList<Integer>(test * 2);

        for (int i = 0; i < test * 2; i += 2){
            int candy = scanner.nextInt();
            int sibling = scanner.nextInt();
            int get_candy = candy / sibling;
            int rest_candy = candy % sibling;

            result.add(i, get_candy);
            result.add(i + 1, rest_candy);
        }

        for (int j = 0; j < test * 2; j += 2){
            System.out.print("You get ");
            System.out.print(result.get(j));
            System.out.print(" piece(s) and your dad gets ");
            System.out.print(result.get(j + 1));
            System.out.println(" piece(s).");
        }


        scanner.close();

    }
}
