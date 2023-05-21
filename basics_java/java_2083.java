/* 2083
 * 17세 초과, 80kg 이상이면 성인부
 * 클럽 회원들 분류하기
 */

 import java.util.*;
 public class java_2083 {
     public static void main(String[] args){
         Scanner scanner = new Scanner(System.in);
         List<String> names = new ArrayList<String>();
         List<String> rating = new ArrayList<String>();
         
         while (true) {
             String name = scanner.next();
             int age = scanner.nextInt();
             int weight = scanner.nextInt();
 
             if ((name.equals("#")) && (age == 0) && (weight == 0)){
                 break;
             }
 
             if ((age > 17) || (weight >= 80)) {
                 rating.add("Senior");
             }
             else {
                 rating.add("Junior");
             }
             names.add(name);
         }
 
         for (int i = 0; i < names.size(); i++){
             System.out.print(names.get(i));
             System.out.print(" ");
             System.out.println(rating.get(i));
         }
         
         scanner.close();
     }
 }