/* ThrowableTest.java
 */

public class ThrowableTest
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
            reader.close();
            System.out.println("--- File End ---");
        } catch (FileNotFoundException e) {
            //do something clever with the exception
        } catch (IOException e) {
            //do something clever with the exception
        } catch (Throwable t) {
            /* TODO
            */
        }
    }
}
