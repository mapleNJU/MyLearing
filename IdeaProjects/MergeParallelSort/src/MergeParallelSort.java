public class MergeParallelSort extends Thread{
    private int a[];
    private int temp[];
    private int low;
    private int high;
    public MergeParallelSort(int arr[],int t[],int lo,int hi){
        a=arr;
        temp=t;
        low=lo;
        high=hi;
    }
    void mergesort()throws Exception{
        int mid=(low+high)/2;
        if(low==high) return ;
        try{
            MergeParallelSort M1=new MergeParallelSort(a,temp,low,mid);
            MergeParallelSort M2=new MergeParallelSort(a,temp,mid+1,high);
            M1.start();
            M2.start();

            M1.join();
            M2.join();
        }
        catch(NullPointerException e){
            System.err.println("Exception is"+e.toString());
        }
        catch(InterruptedException e){
            System.err.println("Exception is"+e.toString());
        }

        //相当于copy数组
        for(int i=low;i<=high;i++)
            temp[i]=a[i];

        int i = low, k = low;
        int j = mid+1;

        //合并数组
        while ((i <= mid) && (j <= high)){
            if (temp[i] < temp[j]){
                a[k++] = temp[i++];
            }
            else if (temp[i] > temp[j]){
                a[k++] = temp[j++];
            }
        }
        while (i <= mid)
            a[k++] = temp[i++];
        while (j <= high)
            a[k++] = temp[j++];
    }
    public void run (){
        try{
            System.out.println( "*************" + Thread.currentThread().getName());
            mergesort();}
        catch(Exception e){
            System.err.println("Exception"+e.toString());
        }
    }

    public static void main(String[] args) throws Exception {
        int[] arr = new int[10000];
        for(int i=0; i<arr.length;i++)  arr[i] = (int)(10000*Math.random());
        int [] t=new int[arr.length];
        int lo=0;
        int hi=arr.length-1;
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        MergeParallelSort a=new MergeParallelSort(arr, t, lo, hi);

        System.out.println("-------------------------");
        a.start();
        a.join();

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}

