/* 29863
 * 첫 번째 줄: 20 ~ 23, 0 ~ 3 : 잠드는 시간
 * 두 번째 줄: 5 ~ 10, 깨어나는 시간
 * 잠 자는 시간 출력하기
 * 어디가 틀렸는지 모르겠음(추후 수정 23.10.03) > 수정 완료(23.10.09)
 */
import java.util.*;
public class java_29863 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int sleep = scanner.nextInt();
        int wake = scanner.nextInt();

        int hour = (24 - sleep) + wake;

        if (hour >= 24) {
            hour -= 24;
        }
        System.out.println(hour);
        
        scanner.close();
    }
}
