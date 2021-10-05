import java.util.Scanner;

class fibonacci {
    public static void main(String[] args) {
        int range, a = 0, b = 1, c;
        System.out.print("Enter the range ");
        Scanner r = new Scanner(System.in);
        range = r.nextInt();
        for (int i = 1; i <= range; i++) {
            System.out.print(a+" ");
            c = a + b;
            a = b;
            b = c;
        }

    }
}