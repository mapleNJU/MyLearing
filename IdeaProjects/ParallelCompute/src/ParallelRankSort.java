import java.util.List;
import java.util.Vector;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveAction;

public class ParallelRankSort extends RecursiveAction{

    private int[] arr;
    private int start;
    private int end;
    private int index;
    private int[] result;

    public ParallelRankSort(int[] arr, int start, int end, int index, int[] result) {
        this.arr = arr;
        this.start = start;
        this.end = end;
        this.index = index;
        this.result = result;
    }


    @Override
    protected void compute() {
        if (index == -1) {
            List<ParallelRankSort> futures = new Vector<>();
            for (int i = start; i <= end; i++) {
                final ParallelRankSort newTask = new ParallelRankSort(arr, start, end, i ,result);
                futures.add(newTask);
            }
            invokeAll(futures);
        }
        else{
            int k = 0;
            for (int j : arr) {
                if (arr[index] > j)
                    k++;
            }
            result[k] = arr[index];
        }
    }
    public static int[] parallel_rank_sort(int[] arr) {
        int[] re = new int[arr.length];
        final ForkJoinPool forkJoinPoolEsp = new ForkJoinPool(Runtime.getRuntime().availableProcessors());
        forkJoinPoolEsp.invoke(new ParallelRankSort(arr, 0, arr.length-1, -1, re));
        return re;
    }
}
