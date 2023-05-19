import java.util.*;

public class CandidateCode {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        int var = arr[n - x];
        int c = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] >= var) {
                c++;
            } else {
                break;
            }
        }
        int ans = -1;
        if (c == x) {
            ans = var;
        }
        System.out.println(ans);
    }
}