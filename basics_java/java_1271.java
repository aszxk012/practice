/* 1271
 * 돈을 생명체에게 똑같이 분배하기
 * 얼마씩 줄 수 있으며, 분배 후 남은 돈 출력하기
 */

import java.math.BigInteger;
import java.util.*;
public class java_1271 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        BigInteger money = scanner.nextBigInteger();
        BigInteger person = scanner.nextBigInteger();

        BigInteger how_money = money.divide(person);
        BigInteger rest_money = money.remainder(person);

        System.out.println(how_money);
        System.out.println(rest_money);
        
        scanner.close();
    }
}
