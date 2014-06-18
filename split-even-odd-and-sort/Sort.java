public class Sort {
    static final String PI = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823";
    /**
     * @param args
     */
    public static void main(String[] args) {
        int upper = 0;
        int lower = 0;
        int p = 0;
        int[] num = new int[100];
        for (int i = 0; i < 100; i++) {
            num[i] = PI.charAt(i) - '0';
        }
        int i = 0;
        while (lower + upper < 100) {
            if (num[i] % 2 == 0) {
                for (p = 100 - 1; p >= 100 - upper; p--) {
                    if (num[p] < num[i])
                        break;
                }
                for (int j = i; j < p; j++) {
                    int t = num[j];
                    num[j] = num[j + 1];
                    num[j + 1] = t;
                }
                upper++;
            } else {
                for (p = 0; p < lower; p++) {
                    if (num[p] > num[i])
                        break;
                }
                // int cache = num[p];
                for (int j = i; j > p; j--) {
                    int t = num[j];
                    num[j] = num[j - 1];
                    num[j - 1] = t;
                }
                i++;
                lower++;
            }
        }
        for (i = 0; i < 100; i++) {
            System.out.print(num[i]);
        }
    }
}