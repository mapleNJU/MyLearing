import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.Future;
import java.util.concurrent.RecursiveAction;

public class ParallelQuickSort extends RecursiveAction {

    private int[] arr;
    private int left;
    private int right;

    public ParallelQuickSort(int[] arr, int left, int right) {
        this.arr = arr;
        this.left = left;
        this.right = right;
    }

    @Override
    protected void compute() {
        int pivot = QuickSort.partition(arr, left, right);//调用串行程序中的partition函数
        ParallelQuickSort task1 = null;
        ParallelQuickSort task2 = null;
        if (pivot - left > 1) {
            task1 = new ParallelQuickSort(arr, left, pivot-1);
            task1.fork();
        }
        if (right - pivot > 1) {
            task2 = new ParallelQuickSort(arr, pivot+1, right);
            task2.fork();
        }
        if (task1 != null && !task1.isDone()) {
            task1.join();
        }
        if (task2 != null && !task2.isDone()) {
            task2.join();
        }
    }

    public static void parallel_quick_sort(int[] arr) {
        ForkJoinPool forkJoinPool = new ForkJoinPool();
        ParallelQuickSort task = new ParallelQuickSort(arr, 0, arr.length-1);
        Future<Void> result = forkJoinPool.submit(task);
        try {
            result.get();
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
}
