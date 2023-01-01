package RoundH2021;
import java.util.Scanner;

public class Painter {
    static Scanner input = new Scanner(System.in);
    public static void main(String[] args) {
        
        // do case print


        // solution
        Solution(6,"BBBYYY");
    }

    public static void Solution(int lengthN, String colorsP) {
        // define colors
        String[] colors = {"U", "R", "Y", "B", "O", "P", "G", "A"};
        String[] colorPalette = new String[lengthN];
        String[] painting = new String[lengthN];
        int minStrokes = 0;
        // TODO: test with string arr, THEN use arraylist
        
        // TODO: finish painting and ret min
        // painting is Uncolored ('U') by default
        for (int i = 0; i < lengthN; i++) {
            painting[i] = colors[0];
        }

        // input of colors used to paint
        colorPalette = colorsP.split("");

        
        // paint the painting and return minimum strokes
        minStrokes = paint(minStrokes, colors, colorPalette, painting);


        for (String string : painting) {
            System.out.println(string);
        }
    }
    // recreate the process 
    // count min number of strokes (Pj)
    private static int paint(int strokes
                                , String[] colors
                                , String[] colorPalette
                                , String[] painting) {

        for (int i = 0; i < painting.length; i++) {
            String c = colorPalette[i];
            switch (c) {
                case "U": painting[i] = colors[0];
                break;
                case "R": painting[i] = colors[1];
                break;
                case "Y": painting[i] = colors[2];
                break;
                case "B": painting[i] = colors[3];
                break;
                case "O": painting[i] = colors[4];
                break;
                case "P": painting[i] = colors[5];
                break;
                case "G": painting[i] = colors[6];
                break;
                case "A": painting[i] = colors[7];
                break;
            }
        }

        return painting;
    }

}