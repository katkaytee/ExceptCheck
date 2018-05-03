/* TryExitTest.java
 */

public class TryExitTest
{
    public void openFile(){
        try {
            // constructor may throw FileNotFoundException
            FileReader reader = new FileReader("someFile");
            int i=0;
            while(i != -1){
                //reader.read() may throw IOException
                i = reader.read();
                System.out.println((char) i );
            }
            if (i == -1) {
                return;
            }
            reader.close();
            System.out.println("--- File End ---");
        } catch (FileNotFoundException e) {
            //do something clever with the exception
            System.out.println("log");
        } catch (IOException e) {
            //do something clever with the exception
        } catch (Throwable t) {
            /* TODO
            */
        } catch (InterruptedException e) {
            System.out.println("log");
        }
    }

    public void test(){
        try {
            int i = 0;
            if (i == 0) {
                return;
            } 
        } catch (Exception e) {}
    }
}
