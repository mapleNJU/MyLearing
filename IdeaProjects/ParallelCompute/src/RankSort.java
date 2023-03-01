public class RankSort {

    static int[] rank_sort(int[] arr){

        int[] result = new int[arr.length];

        for (int k : arr) {
            int index = 0;
            for (int i : arr) {
                if (k > i) {
                    index++;
                }
            }
            result[index] = k;
        }

        return result;
    }
}
