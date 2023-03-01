public class QuickSort {

    public static void quick_sort(int[] a,int left,int right) {
        if(left<right) {
            int temp=partition(a,left,right);
            quick_sort(a,left,temp-1);
            quick_sort(a,temp+1,right);
        }
    }

    public static int partition(int[] a,int left,int right) {
        int temp=a[left];
        while(left<right) {
            while(left<right && a[right]>temp) {
                right--;
            }
            if(left<right) {
                a[left++]=a[right];
            }
            while(left<right && a[left]<=temp) {
                left++;
            }
            if(left<right) {
                a[right--]=a[left];
            }
        }
        a[left]=temp;
        return left;
    }
}

