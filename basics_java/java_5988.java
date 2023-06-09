/* 5988
 * 테스트 케이스 개수만큼 수 입력 받아 짝수, 홀수 판별하기
 */
import java.math.BigInteger;
import java.util.*;
public class java_5988 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();

        for (int i = 0; i < test; i++) {
            BigInteger num = scanner.nextBigInteger();
            if (num.remainder(BigInteger.valueOf(2)).intValue() != 0){
                System.out.println("odd");
            }
            else {
                System.out.println("even");
            }
        }
        scanner.close();
    }
}
