/* 백준에서 채점할 때 class명은 무조건 Main
 * 4999
 * 첫째줄은 가장 길게 낼수 있는 aah
 * 두번째줄은 의사가 듣길 원하는 aah > 판단을 내릴 수 있는 최소한의 값
 * 병원을 가야하는지 말아야하는지 판단하기
 */

import java.util.Scanner;

public class java_4999 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String sound = scanner.next();
        String sound_dr = scanner.next();

        if(sound.length() >= sound_dr.length()) {
            System.out.println("go");
        }
        else if(sound.length() < sound_dr.length()) {
            System.out.println("no");
        }
    }
}