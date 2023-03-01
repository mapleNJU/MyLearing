import java.io.File;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.util.Random;

public class Demo {

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

    public static void main(String[] args) {
        int[] values = new int[300000];
        Random random = new Random();

        for(int i = 0;i < values.length;i++){
            int number = random.nextInt(1000000) -500000;
                    values[i]=number;
        }
        outputToTxt(1,values);
    }
}
