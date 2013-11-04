/* 
 * CuGBabyBeaR  
 */

public class Puddle{

    public static void main(String[] args) {
        int [] testcase_1 = {2,5,1,2,3,4,7,7,6};
        int [] testcase_2 = {2,5,1,3,1,2,1,7,7,6};
        int [] testcase_3 = {6,1,4,6,7,5,1,6,4};

        System.out.println("Case testcase_1, total volume :" + calculate(testcase_1));
        System.out.println("Case testcase_2, total volume :" + calculate(testcase_2));
        System.out.println("Case testcase_3, total volume :" + calculate(testcase_3));
    }

    private static int calculate(int [] testcase){
        int p_l = 0;
        int p_r = testcase.length - 1;
        int max_l = testcase[p_l];
        int max_r = testcase[p_r];

        int volume = 0;
        while (p_r > p_l) {
            if (max_l < max_r){
                p_l++;
                if (testcase[p_l] >= max_l){
                    max_l = testcase[p_l];
                }else{
                    volume += max_l - testcase[p_l];
                }
            }else{
                p_r--;
                if (testcase[p_r] >= max_r){
                    max_r = testcase[p_r];
                }else{
                    volume += max_r - testcase[p_r];
                }
            }
        }

        return volume;
    }
}
