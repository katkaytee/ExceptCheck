/* Division.java
 */

public class Division
{
    public void callDivide(){
        try {
            int result = divide(2,1);
            System.out.println(result);
        } catch (BadNumberException e) {
            //do something clever with the exception
            System.out.println(e.getMessage()).log();
        }
        System.out.println("Division attempt done");
    }

    public void callDivideTODO(){
        try {
            int result = divide(2,1);
            System.out.println(result);
        } catch (BadNumberException e) {
            //do something clever with the exception
            // TODO
            /* FIXME */
            System.out.println(e.getMessage());
            log.abort();
        }
        System.out.println("Division attempt done");
    }
}
