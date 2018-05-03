/* IfCheckTest.java
 */

public class IfCheckTest
{
    public void variableTest() {
    	int i = 0;
    	try {
            // constructor may throw FileNotFoundException
            FileReader reader = new FileReader("someFile");
            i = reader.read();
            System.out.println((char)i);
            
            reader.close();
            System.out.println("--- File End ---");
        } catch (Exception e) {
        	// Empty because we have an if check following this.
        }
        if (i) {
            return;
        } 
    }

    public void binaryTest() {
        int i = 0;
        try {
            // constructor may throw FileNotFoundException
            FileReader reader = new FileReader("someFile");
            i = reader.read();
            System.out.println((char)i);
            
            reader.close();
            System.out.println("--- File End ---");
        } catch (Exception e) {
            // Empty because we have an if check following this.
        }
        if (i == -1) {
            return;
        } 
    }

    public void methodTest() {
        int i = 0;
        try {
            // constructor may throw FileNotFoundException
            FileReader reader = new FileReader("someFile");
            i = reader.read();
            System.out.println((char)i);
            
            reader.close();
            System.out.println("--- File End ---");
        } catch (Exception e) {
            // Empty because we have an if check following this.
        }
        if (handle(i)) {
            return;
        } 
    }
}
