/* 1924
 * 2007년 x월 y일은 무슨 요일인지 출력하기
 */

import java.util.*;
import java.time.*;
public class java_1924 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int year = 2007;
        int month = scanner.nextInt();
        int day = scanner.nextInt();

        LocalDate date = LocalDate.of(year, month, day);
        DayOfWeek dayOfWeek = date.getDayOfWeek();
        int day_number = dayOfWeek.getValue();
        String day_of_week = "";

        if (day_number == 1) {
            day_of_week = "MON";
        }
        else if (day_number == 2) {
            day_of_week = "TUE";
        }
        else if (day_number == 3) {
            day_of_week = "WED";
        }
        else if (day_number == 4) {
            day_of_week = "THU";
        }
        else if (day_number == 5) {
            day_of_week = "FRI";
        }
        else if (day_number == 6) {
            day_of_week = "SAT";
        }
        else {
            day_of_week = "SUN";
        }

        System.out.println(day_of_week);
        scanner.close();
    }
}
