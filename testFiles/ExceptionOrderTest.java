/* ExceptionOrderTest.java
 */

public class ExceptionOrderTest
{
    public void test() {
    	int i = 0;
    	try {
            // constructor may throw FileNotFoundException
            FileReader reader = new FileReader("someFile");
            i = reader.read();
            System.out.println((char)i);
            
            reader.close();
            System.out.println("--- File End ---");
        } catch (Exception e) {
        	// Empty 
            // TODO
        } catch (IOException e) {
            // This is really wrong
        }
    }
}
