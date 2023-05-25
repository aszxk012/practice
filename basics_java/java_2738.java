/* 2738
 * 행렬 덧셈
 */

 import java.util.*;
 public class java_2738 {
     public static void main(String[] args){
         Scanner scanner = new Scanner(System.in);
         int a = scanner.nextInt();
         int b = scanner.nextInt();
         int matrix1[][] = new int[a][b];
         int matrix2[][] = new int[a][b];
         int result[][] = new int[a][b];
 
         for (int i = 0; i < a; i++) {
             for (int j = 0; j < b; j++){
                 matrix1[i][j] = scanner.nextInt();
             }
         }
 
         for (int i = 0; i < a; i++) {
             for (int j = 0; j < b; j++){
                 matrix2[i][j] = scanner.nextInt();
             }
         }
 
         for (int i = 0; i < a; i++){
             for (int j = 0; j < b; j++){
                 result[i][j] = matrix1[i][j] + matrix2[i][j];
                 System.out.print(result[i][j]);
                 System.out.print(" ");
             }
             System.out.println();
         }
         
         scanner.close();
     }
 }
 