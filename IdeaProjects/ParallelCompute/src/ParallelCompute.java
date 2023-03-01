import java.io.*;
import java.util.Arrays;
import java.util.Scanner;

public class ParallelCompute {

    static int MAX=30000;//这里需要根据当前数据量来更改

    public static int[] ReadTxt(){

        int[] data = new int[MAX];
        int[] raw_data = new int[MAX];
        File inputFile = new File("random.txt");
        int index = 0;
        FileInputStream fileInputStream;
        try {
            fileInputStream = new FileInputStream(inputFile);
            Scanner scanner = new Scanner(fileInputStream);
            while (scanner.hasNext()){
                raw_data[index++] = scanner.nextInt();
            }
            fileInputStream.close();
            System.arraycopy(raw_data, 0, data, 0, raw_data.length);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return data;
    }

    public static void outputToTxt(int id, int[] arr){
        try {
            File outputFile = new File("order" + String.valueOf(id) + ".txt");
            if (outputFile.exists())
                outputFile.delete();
            outputFile.createNewFile();
            FileOutputStream fileOutputStream = new FileOutputStream(outputFile);
            PrintStream printStream = new PrintStream(fileOutputStream);
            for (int j : arr) {
                printStream.print(j + " ");
            }
            printStream.close();
            fileOutputStream.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args){
        int[] arr=ReadTxt();

        int[] newArr1 = Arrays.copyOf(arr,arr.length);
        int[] newArr2 = Arrays.copyOf(arr,arr.length);
        int[] newArr3 = Arrays.copyOf(arr,arr.length);
        int[] newArr4 = Arrays.copyOf(arr,arr.length);
        int[] newArr5 = Arrays.copyOf(arr,arr.length);
        int[] newArr6 = Arrays.copyOf(arr,arr.length);

        long start,end;

        start=System.currentTimeMillis();
        QuickSort.quick_sort(newArr1,0,newArr1.length-1);
        end=System.currentTimeMillis();
        outputToTxt(1, newArr1);
        System.out.println("Quick Sort: "+(end-start)+"ms.");

        start=System.currentTimeMillis();
        MergeSort.merge_sort(newArr2,0,newArr2.length-1);
        end=System.currentTimeMillis();
        outputToTxt(2, newArr2);
        System.out.println("Merge Sort: "+(end-start)+"ms.");


        start=System.currentTimeMillis();
        int[] arr3=RankSort.rank_sort(newArr3);
        end=System.currentTimeMillis();
        outputToTxt(3, arr3);
        System.out.println("Rank Sort: "+(end-start)+"ms.");


        start=System.currentTimeMillis();
        ParallelQuickSort.parallel_quick_sort(newArr4);
        end=System.currentTimeMillis();
        outputToTxt(4, newArr4);
        System.out.println("Parallel Quick Sort: "+(end-start)+"ms.");

        start=System.currentTimeMillis();
        ParallelMergeSort.parallel_merge_sort(newArr5);
        end=System.currentTimeMillis();
        outputToTxt(5, newArr5);
        System.out.println("Parallel Merge Sort: "+(end-start)+"ms.");

        start=System.currentTimeMillis();
        int[] arr6=ParallelRankSort.parallel_rank_sort(newArr6);
        end=System.currentTimeMillis();
        outputToTxt(6, arr6);
        System.out.println("Parallel Rank Sort: "+(end-start)+"ms.");

    }
}
