import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.Future;
import java.util.concurrent.RecursiveAction;

public class ParallelMergeSort extends RecursiveAction {
    private int[] array;
    private int left;
    private int right;

    public ParallelMergeSort(int[] array, int left, int right) {
        this.array = array;
        this.left = left;
        this.right = right;
    }

    @Override
    protected void compute() {
        int mid = (left + right)/2;
        if (right - left >= 1) {
            ParallelMergeSort mergeSortTask1 = new ParallelMergeSort(array, left, mid);
            ParallelMergeSort mergeSortTask2 = new ParallelMergeSort(array, mid+1, right);
            mergeSortTask1.fork();
            mergeSortTask2.fork();
            mergeSortTask1.join();
            mergeSortTask2.join();
        }
        MergeSort.merge(array, left, mid, right);//调用串行程序中的merge函数
    }

    public static void parallel_merge_sort(int[] arr) {
        ForkJoinPool forkJoinPool = new ForkJoinPool();
        ParallelMergeSort task = new ParallelMergeSort(arr, 0, arr.length-1);
        Future<Void> result = forkJoinPool.submit(task);
        try {
            result.get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
}