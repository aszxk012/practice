/* 11718
 * 입력받은 그대로 출력하기
 * EOF
 */

import java.util.*;

public class java_11718 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        List<String> result = new ArrayList<String>();

        while (scanner.hasNext()){
            result.add(scanner.nextLine());
        }

        for(int i = 0; i < result.size(); i++){
            System.out.println(result.get(i));
        }
        scanner.close();
    }
}
