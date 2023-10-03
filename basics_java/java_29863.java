/* 29863
 * 어디가 틀렸는지 모르겠음(추후 수정 23.10.03)
 */
import java.util.*;
public class java_29863 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int sleep = scanner.nextInt();
        int wake = scanner.nextInt();

        int hour = (24 - sleep) + wake;

        System.out.println(hour);
        
        scanner.close();
    }
}
