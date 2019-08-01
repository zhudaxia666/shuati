import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String str1;
        String str2;
        str1 = scanner.nextLine();
        str2 = scanner.nextLine();
        String strs1[] = str1.split(" ");
        String strs2[] = str2.split(" ");
        int A[] = new int[strs1.length];
        int B[] = new int[strs2.length];
        for(int i = 0;i<strs1.length;i++){
            A[i] = Integer.parseInt(strs1[i]);
        }
        for(int i = 0;i<strs2.length;i++){
            B[i] = Integer.parseInt(strs2[i]);
        }
        Arrays.sort(B);
        int pos = -1;
        for(int i = 1;i<A.length;i++){
            if(A[i]<=A[i-1]){
                pos = i-1;
                break;
            }
        }
        int ans = Integer.MIN_VALUE;
        int val1 = pos-1==-1?Integer.MIN_VALUE:A[pos-1];
        int val2 = pos+1>=A.length?Integer.MAX_VALUE:A[pos+1];
        int val3 = A[pos];
        int val4 = pos+2>=A.length?Integer.MAX_VALUE:A[pos+2];
        int ans_pos = 0;
        for(int i = 0;i<B.length;i++){
            if(B[i]>val1&&B[i]<val2){
                if(B[i]>ans){
                    ans_pos = pos;
                }
                ans=Math.max(ans,B[i]);

            }
            if(B[i]>val3 && B[i]<val4){
                if(B[i]>ans){
                    ans_pos = pos+1;
                }
                ans=Math.max(ans,B[i]);
            }

        }
        if(ans==Integer.MIN_VALUE){
            System.out.println("NO");
        }else{
            A[ans_pos] = ans;
            for(int i = 0;i<A.length;i++){
                System.out.print(A[i]+" ");
            }
        }
    }
}