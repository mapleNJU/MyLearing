public class EnumSort {

    public static void main(String[] args) {
        int[] arr = {11,44,23,67,88,65,34,48,9,12};
        int[] newarr = new int[arr.length];    //新建一个临时数组存放
        enumsort(arr,0,arr.length-1,newarr);
        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }
    }

    public static void enumsort(int arr[],int low,int high,int newarr[]){
        for(int i=0;i<high+1;i++){
            int tmp=0;
            for(int j=0;j<high+1;j++){
                if (arr[i]>arr[j]){
                    tmp+=1;
                }
            }
            newarr[tmp]=arr[i];//need to consider having many same figures.
        }

        for(int i=0;i<high+1;i++){
            arr[i]=newarr[i];
        }
    }
}
