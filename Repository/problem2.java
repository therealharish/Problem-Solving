import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }
        int[] queries = new int[m];
        for (int i = 0; i < m; i++) {
            queries[i] = scanner.nextInt();
        }

        int[] newArr = new int[n + 2];
        Arrays.sort(arr);
        for (int i = 0; i < n; i++) {
            newArr[i + 1] = arr[i] + newArr[i];
        }

        List<Integer> ans = new ArrayList<>();
        for (int i : queries) {
            int l = 0;
            int r = arr.length - 1;
            int best = -1;
            while (l <= r) {
                int mid = (l + r) / 2;
                if (arr[mid] <= i) {
                    best = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            int var = best;
            int sum1 = newArr[var + 1];
            int sum2 = newArr[n];

            if (var != -1) {
                sum2 -= newArr[var + 1];
            }

            ans.add(((var + 1) * i - sum1) + (sum2 - (n - var - 1) * i));
        }

        System.out.println(ans.toString().replaceAll("[\\[\\],]", ""));
    }
}