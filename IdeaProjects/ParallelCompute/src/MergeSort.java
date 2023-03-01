public class MergeSort {

    public static void merge(int[] arr, int left, int mid, int right) {
        int len = right - left + 1;
        int[] temp = new int[len];
        int i = left;
        int j = mid + 1;
        int index = 0;
        while (i <= mid && j <= right) {
            temp[index++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
        }
        while (i <= mid) {
            temp[index++] = arr[i++];
        }
        while (j <= right) {
            temp[index++] = arr[j++];
        }
        for (int value : temp) {
            arr[left++] = value;
        }
    }

    public static void merge_sort(int[] arr, int left, int right) {
        if (left < right) {   // 说明至少还存在两个元素：需要进行分
            int mid = (left + right) / 2;       // 获得中间位置的下标(偏左)
            merge_sort(arr, left, mid);          // 分操作：对左半部分的子序列递归调用
            merge_sort(arr, mid+1, right);   // 分操作：对右半部分的子序列递归调用
            merge(arr,left,mid,right); // 治操作：解决有序两个子序列的合并
        }
    }
}
